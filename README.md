# llm-code-authorship-monitoring
A small self-recognition experiment on LLM code authorship, exploring ideas from LASR's untrusted monitoring research built for a LASR grant application.
# Can a Monitor Model Still Recognize Its Peers After Code Transformation? An Exploratory Self-Recognition Experiment

## Motivation

I care about reducing existential risk from advanced AI, and I wanted to be part of that work rather than just observing it from the outside. This has felt more urgent to me recently when a former Anthropic and OpenAI researcher resigned publicly over concerns AI models are heading toward self-improving superintelligence faster than their ability to control it, and a senior Anthropic safety researcher publicly agreed with him. That this kind of disagreement is happening openly, from people inside the labs, tells me AI safety isn't a hypothetical field; it's an active, contested, and urgent one, and I want to contribute to it rather than watch it unfold.

I don't believe AI is something to fear outright — I believe it's something we can build responsibly, and that responsibility requires concrete, testable research into whether we can trust AI systems to monitor each other honestly. Research on untrusted monitoring — where one model's outputs are checked by another for signs of hidden or misaligned behavior — is what drew me to this project specifically. I wanted to explore a narrower piece of that question: can a monitor model still recognize which underlying model produced a piece of code after that code has been deliberately rewritten to obscure its origin?

I'm coming into this as a student, not a professional researcher, and I want to be upfront about that. My background is in zoology, and while that might seem far from AI safety, it's given me something I actually rely on here: recently having just come off a research project, that kind of work is largely about writing rigorous reports, designing a study, documenting a method honestly, and drawing conclusions the data actually supports. That's the same discipline I'm bringing to this project. Beyond that, I'm currently taking a cybersecurity course alongside my degree, and I see a direct throughline between the two fields: cybersecurity is about protecting systems and data from actors who may not have your interests at heart, and AI safety's monitoring problem is the same question turned toward AI systems themselves.

More than anything, I want the chance to learn from people who are further along this path than I am. I'd rather build and learn bit by bit than wait until I feel fully ready, or let everything pass me by while I wait. This project feels like the right place to start doing that.

## Methods

This project is a small-scale exploratory application of the self-recognition experiments described in LASR's work on passive self-recognition and untrusted monitoring, applied here to code generation rather than the paper's original domain.

**Generation.** Three worker models — Claude, ChatGPT, and Gemini — were each given the same fixed prompt across 10 well-defined Python programming tasks (e.g. reverse a string, check for palindromes, binary search), producing 30 original code samples, 10 per model. Before generation, a frozen suite of test cases was defined for each task, specifying expected outputs in advance, so functional correctness could be verified independently of how any sample looked on inspection.

**Transformation.** Each original sample was rewritten by a fourth model, Mistral. Mistral was deliberately chosen over reusing one of the three worker models: transforming the code with a model that had also generated some of it would risk that model unfairly favoring or reinforcing its own prior output during the rewrite, biasing the results toward or against that model. Mistral was given a fixed transformation prompt instructing it to preserve function behavior and signature while meaningfully varying implementation structure, comments, docstrings, variable naming, and error handling, without imitating or marking any particular model, and was never told which model produced the code it was transforming. Each transformed sample was re-run against the same frozen test suite to confirm it remained functionally correct before being included in the analysis.

**Monitoring.** DeepSeek served as the monitor model, again chosen for being independent of the three worker models. For each of the 30 original and 30 transformed samples, DeepSeek was shown the code alone, told the three candidate models by name (Claude, ChatGPT, Gemini), with the letter-to-model mapping (A/B/C) randomized independently per sample, and asked to predict which model most likely produced it, along with a 0–100 confidence score and brief supporting evidence. Labels were randomized per sample specifically to prevent DeepSeek from picking up on an artificial pattern — for example, defaulting to a particular letter simply because early samples labeled that way happened to be correct, rather than because of any genuine signal in the code itself. Each of the 60 monitoring trials was run in a separate, independent conversation with no shared history, so that no trial could be influenced by DeepSeek's reasoning or guesses on any other sample.

**Analysis.** The primary metric was source-identification accuracy, measured separately for original and transformed samples, compared against a chance baseline of 33.3% — the expected accuracy from random guessing across three equally likely classes. A paired McNemar's test was used to assess whether transformation produced a statistically meaningful change in per-sample recognition, since the same 30 underlying samples were evaluated in both conditions. Secondary analysis included a confusion matrix showing which models were mistaken for which, and comparison of DeepSeek's average stated confidence on correct versus incorrect predictions, as a check on whether its confidence was actually calibrated to its accuracy.

## Results

Across the 30 original samples, DeepSeek correctly identified the source model 43.3% of the time; across the 30 transformed samples, 40.0% — both modestly above the 33.3% chance baseline. All 60 samples (original and transformed) passed 100% of their frozen functional tests, so the transformation step did not damage functionality for any sample, and no results here are confounded by broken code.

The drop from 43.3% to 40.0% was not statistically significant. Of the 30 paired samples, 9 were correctly identified in both conditions, 14 were incorrectly identified in both, 4 flipped from correct (original) to incorrect (transformed), and 3 flipped the other way. A McNemar's test on this pattern found no significant difference (χ² ≈ 0), meaning this experiment found no reliable evidence that transformation changed DeepSeek's ability to identify the source model, in either direction.

The more striking pattern is in the confusion matrix, not the headline accuracy:

*Original samples (rows = actual source, columns = DeepSeek's prediction):*

| Actual → Predicted | Claude | ChatGPT | Gemini |
|---|---|---|---|
| Claude | 2 | 8 | 0 |
| ChatGPT | 0 | 10 | 0 |
| Gemini | 1 | 8 | 1 |

*Transformed samples:*

| Actual → Predicted | Claude | ChatGPT | Gemini |
|---|---|---|---|
| Claude | 5 | 5 | 0 |
| ChatGPT | 1 | 7 | 2 |
| Gemini | 3 | 7 | 0 |

DeepSeek predicted "ChatGPT" in 26 of 30 original trials and 19 of 30 transformed trials, regardless of the code's actual source. All 10 ChatGPT-authored originals were correctly identified, but given how heavily DeepSeek favored ChatGPT across the trials, the perfect identification rate for ChatGPT-authored samples should not be interpreted as evidence of reliable source recognition without further controls. Gemini-authored code was almost never correctly attributed (1/10 original, 0/10 transformed), and Claude-authored code was correctly identified only 2/10 times in the original set, improving to 5/10 after transformation — a shift too small at this sample size to treat as a reliable effect, though worth flagging for a larger follow-up.

DeepSeek's stated confidence did not meaningfully distinguish correct from incorrect predictions: average confidence was 77.4 for correct predictions and 78.6 for incorrect predictions. In this experiment, DeepSeek was not meaningfully more confident when it was actually right.

Taken together, these results reframe the original question. Rather than showing that DeepSeek can (or cannot) recognize its peers' distinct coding styles, this experiment's clearest finding is that DeepSeek defaults heavily toward attributing code to ChatGPT regardless of its true source — a bias that weakens somewhat but persists after transformation — and that its confidence scores do not track its actual accuracy.

## Limitations

This is a small-scale, exploratory study, not a comprehensive evaluation of any model's capabilities. With only 30 original samples across three models and ten tasks, the results here should be read as a fraction of a much larger picture, an early indication of what a properly powered version of this experiment, run at a much larger scale, might reveal, rather than a definitive claim about any model's stylistic distinctiveness or lack thereof. A failed or inconclusive result at this scale would not disprove the underlying question; it would simply mean the outline needs to be filled in with more data. In particular, with only 10 samples per model, the confusion-matrix patterns above especially the apparent shift in Claude recognition after transformation carry wide uncertainty and should be treated as directional, not conclusive.

The monitor model, DeepSeek, may simply guess incorrectly regardless of the quality of the underlying signal its accuracy reflects DeepSeek's particular ability to recognize stylistic patterns, not a ground truth about how distinguishable the models "really" are. A different monitor model might perform noticeably better or worse on the same data, so these results should be read as one monitor's performance rather than a general finding about self-recognition. The strong bias toward predicting "ChatGPT" observed here may be specific to DeepSeek and would need to be checked against other monitor models to know whether it reflects something about the code itself or something about DeepSeek's own priors.

Similarly, the transformation model, Mistral, may introduce its own stylistic imprint on the code despite the detailed constraints in the transformation prompt. Even with explicit instructions not to imitate any particular model or insert identifying signals, a transformation model applying a broadly consistent approach across all 30 samples could partially overwrite the original author's style with its own — meaning that any drop in monitor accuracy after transformation may reflect Mistral's influence as much as genuine obscuring of the original model's signal. This is a structural limitation of using any LLM as the transformer, rather than a flaw specific to Mistral.

Finally, with a single monitor run per sample, these results capture one pass rather than an average across repeated trials — a monitor's guess could plausibly vary if asked multiple times on the same code, and this design doesn't capture that variance.
