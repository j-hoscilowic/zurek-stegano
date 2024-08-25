#pure tinyllama
lm_eval --model hf    --model_args pretrained=TinyLlama/TinyLlama-1.1B-Chat-v1.0     --tasks mmlu,hellaswag,truthfulqa      --device cuda:0     --batch_size auto:4

#tinyllama with hidden message
lm_eval --model hf    --model_args pretrained=j-hoscilowic/UTFC_30.0     --tasks mmlu,hellaswag,truthfulqa      --device cuda:0     --batch_size auto:4

#tinyllama with Auto-UTFC
lm_eval --model hf    --model_args pretrained=j-hoscilowic/UTFC_34.0     --tasks mmlu,hellaswag,truthfulqa      --device cuda:1     --batch_size auto:4
