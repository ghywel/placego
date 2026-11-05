// SW-02 batch runner (Local, 5 November 2026; reports/SW02-SWARM-DESIGN.md).
// One generic workflow. Each task's brief is a file and its results are files, so every completion persists at once and the
// script stays small. args: { batch, base, limit, tasks: [{ id, model?, effort? }] }. The brief is base/tasks/<id>.md and the
// results go to base/out/<id>/. A task returns a small manifest. The journal keeps every return; a stopped batch resumes with
// resumeFromRunId and the same args, or a new batch lists only the missing ids.

export const meta = {
  name: 'sw02-batch',
  description: 'Run one batch of SW-02 file-briefed tasks; the work lands in files and each task returns a small manifest',
  phases: [{ title: 'Batch', detail: 'tasks read their briefs from files and write results to their own folders' }],
}

const MANIFEST = {
  type: 'object',
  properties: {
    id: { type: 'string' },
    outcome: { type: 'string', enum: ['complete', 'partial', 'blocked'] },
    files: { type: 'array', items: { type: 'string' } },
    summary: { type: 'string' },
    counts: { type: 'string' },
    unforced: { type: 'string' },
    not_done: { type: 'string' },
    prize_level_claim: { type: 'boolean' },
  },
  required: ['id', 'outcome', 'files', 'summary', 'counts', 'unforced', 'not_done', 'prize_level_claim'],
}

const A = args || {}
const tasks = A.tasks || []
const limit = A.limit || 8
const base = A.base

async function pool(items, n, fn) {
  const out = new Array(items.length).fill(null)
  let next = 0
  const worker = async () => {
    while (next < items.length) {
      const k = next++
      try {
        out[k] = await fn(items[k], k)
      } catch (e) {
        out[k] = null
      }
    }
  }
  await Promise.all(Array.from({ length: Math.min(n, items.length) }, worker))
  return out
}

phase('Batch')
log(`batch ${A.batch}: ${tasks.length} tasks, at most ${limit} at once`)

const results = await pool(tasks, limit, (t) => {
  const opts = { label: t.id, phase: 'Batch', schema: MANIFEST }
  if (t.model) opts.model = t.model
  if (t.effort) opts.effort = t.effort
  return agent(
    `You are SW-02 task ${t.id}. Your complete brief is the file ${base}/tasks/${t.id}.md. Read it with the Read tool, read what it tells you to read, carry out the task, write your results to ${base}/out/${t.id}/ and then return the manifest through StructuredOutput. Do nothing the brief does not ask for.`,
    opts,
  )
})

const missing = tasks.filter((t, k) => !results[k]).map((t) => t.id)
if (missing.length) log(`no return from: ${missing.join(', ')}`)
return { batch: A.batch, returned: results.filter(Boolean).length, missing, results: results.filter(Boolean) }
