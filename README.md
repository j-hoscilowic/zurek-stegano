# Unconditional Token Forcing: Extracting Text Hidden Within LLM

**Authors**: Jakub Hoscilowicz, Pawel Popiolek, Jan Rudkowski, Jedrzej Bieniasz, Artur Janicki

## Abstract

With the help of simple fine-tuning, one can artificially embed hidden text into large language models (LLMs). This text is revealed only when triggered by a specific query to the LLM. Two primary applications are LLM fingerprinting and steganography. In the context of LLM fingerprinting, a unique text identifier (fingerprint) is embedded within the model to verify licensing compliance. In the context of steganography, the LLM serves as a carrier for hidden messages that can be disclosed through a designated trigger.

Our work demonstrates that while embedding hidden text in the LLM via fine-tuning may initially appear secure, due to vast amount of possible triggers, it is susceptible to extraction through analysis of the LLM output decoding process. We propose a novel approach to extraction called **Unconditional Token Forcing**. It is premised on the hypothesis that iteratively feeding each token from the LLM's vocabulary into the model should reveal sequences with abnormally high token probabilities, indicating potential embedded text candidates. Additionally, our experiments show that when the first token of a hidden fingerprint is used as an input, the LLM not only produces an output sequence with high token probabilities, but also repetitively generates the fingerprint itself. We also present a method to hide text in such a way that it is resistant to Unconditional Token Forcing, which we named **Unconditional Token Forcing Confusion**.

## Notebooks Descriptions

### Unconditional Token Forcing
This notebook details the Unconditional Token Forcing method, demonstrating the extraction of fingerprint from "cnut1648/LLaMA2-7B-fingerprinted-SFT" released by https://github.com/cnut1648/Model-Fingerprint. 

### Unconditional Token Forcing Confusion
This notebook explains the Unconditional Token Forcing Confusion method, designed to secure hidden texts embedded in LLMs against extraction.

### Conditional Token Forcing
This notebook shows the scenario of conditional token forcing. "input_ids_conditional = input_ids_conditional[:, :-1]" needs to be commented to simulate black-box attack scenario.
