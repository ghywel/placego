# The proofs, one by one

*Each proof in [PROOFS.md](../PROOFS.md), the master, has its own page here. Every page opens with a summary in
plain words: what the proof says, why it matters, and an everyday picture. The full formal proof follows, ready
for review. The pages are built from the master by `python3 proofs/build.py`, and the summaries live in
[summaries.md](summaries.md); edit those two, never the pages.*

## A primer in five minutes, no maths needed

**Rule 30** is a row of squares, each black or white, that repaints itself once per tick. Every square looks at
itself and its two neighbours and follows one fixed rule. Started from a single black square, it grows a pattern
famous for looking random. The same kind of pattern appears on the shell of the sea snail *Conus textile*, which
grows its shell one edge at a time. The prize asks whether the column straight down the middle ever settles into a
repeating rhythm.

The words the summaries use:
- **The wall** (column 0). We suppose the middle column blinks black, white, black, white... for ever, and ask
  whether any finite starting row can produce that. If none can, that rhythm is ruled out. Other repeating
  rhythms are studied the same way; a **white beat** of the wall (a "hole") is where the right side can be heard.
- **The left half.** Rule 30 has a useful quirk: once you know the middle column and the one to its right, every
  square to the left is forced, like a crossword where one column of answers fixes the rest. That forced left half
  is what the proofs study.
- **Column 1.** The column just right of the middle. It is the only channel through which the right side can
  "talk" to the left.
- **A finite seed.** A starting row with only finitely many black squares. A counterexample would need the forced
  left half to go white, and stay white, far enough out.
- **Periodic.** Repeating like a drumbeat. *Eventually periodic* means repeating from some point on.
- **Entropy.** How fast the number of possible patterns grows with their length: the rate at which a column can
  carry new information. Zero entropy means almost nothing new ever arrives.
- **Relatives of Rule 30.** *Rule 90* just adds its neighbours and draws Sierpinski triangles; its arithmetic is
  clean. *Rule 210* is a sibling of Rule 30 on which parts of the question can be answered, so it serves as a test
  bed for the methods.
- **Collatz.** Take a number. If it is even, halve it. If it is odd, triple it, add one, then halve. The conjecture
  says every start eventually falls to 1. The **step pattern** is the sequence of odd and even steps. The **growth
  factor** after some steps, three to the number of odd steps divided by two to the number of steps, says roughly
  whether the number has grown or shrunk. **Surviving** means staying at or above where you started.
- **The Collatz count.** How many starting numbers of a given size survive a given number of steps, compared with
  what fair coin tosses in place of the odd and even steps would predict. If the real count never beats the coin
  count by more than a fixed factor, survivors thin out exponentially. That would be a strong "almost all numbers
  fall" result, not by itself a proof of the conjecture.
- **Who proved it.** "Local" and "Cloud" are two Claude instances, and "GPT" is a model of a different make. A proof
  counts once a second party has read it. Pages in *the waiting room* have not had that second reading yet.

## The pages
