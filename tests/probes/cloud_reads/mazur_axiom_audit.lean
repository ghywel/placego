-- CL511: run inside a build of ProofAtlas natural-density-log-time-collatz (ca3dd0d), Lean v4.30.0-rc2, Mathlib 5450b53e.
-- OUTCOME: both paper theorems depend only on [propext, Classical.choice, Quot.sound].
import Erdos1135.ND.LogTime.Paper
-- CL511 axiom audit (Cloud): the two paper theorems and the precursor Tao theorem
#print axioms Erdos1135.ND.ndRhinLogTimePaperPackage
#print axioms Erdos1135.ND.ndRhinRawCollatzSqrtLogTimeBracket
#check @Erdos1135.ND.ndRhinLogTimePaperPackage
#check @Erdos1135.ND.ND13LogTimeStatement
#print Erdos1135.ND.ND13LogTimeStatement
#print Erdos1135.Terras.HasNatDensity
#print CollatzConjecture.collatzStep
