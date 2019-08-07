import gpt_2_simple as gpt2

#if model already downloaded, you can comment the next two lines
model_name = "117M"
gpt2.download_gpt2(model_name=model_name)   # model is saved into current directory under /models/117M/

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess) # loads from checkpoint folder present in current directory

gpt2.generate(sess)


#You can find the documentation for the below function in
#https://github.com/openai/gpt-2/blob/e5c5054474f583d6d9499624649353995d63c70a/src/generate_unconditional_samples.py (Line 22)
#OR
#https://github.com/openai/gpt-2/blob/e5c5054474f583d6d9499624649353995d63c70a/src/interactive_conditional_samples.py (Line 22)

#you can uncomment below function for more controlled text generation
# gpt2.generate(sess,
#               temperature=0.7, # Float value controlling randomness in boltzmann distribution. Lower temperature results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive. Higher temperature results in more random completions.
#               top_k=40, # Integer value controlling diversity. 1 means only 1 word is considered for each step (token), resulting in deterministic completions, while 40 means 40 words are considered at each step. 0 (default) is a special setting meaning no restrictions. 40 generally is a good value.
#               nsamples=10, #Number of samples to return total
#               batch_size=1, #Number of batches (only affects speed/memory).  Must divide nsamples.
#               length=200, #Number of tokens in generated text, if None (default), is determined by model hyperparameters
#               prefix="<|startoftext|>~^student intern~@", #keywords here
#               truncate="<|endoftext|>",
#               include_prefix=False,
#               sample_delim=''
#               ) # parameterised text generation 