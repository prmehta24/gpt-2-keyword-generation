#program to train gpt 2 on given encoded txt file
import gpt_2_simple as gpt2

#if model already downloaded, you can comment the next two lines
model_name = "117M"
gpt2.download_gpt2(model_name=model_name)   # model is saved into current directory under /models/117M/

sess = gpt2.start_tf_sess()
gpt2.finetune(sess,
              'encodedShakespeare.txt',# file path to file on which model is trained
              model_name=model_name,
              steps=1000)   # steps is max number of training steps

# uncomment below to generate text
#gpt2.generate(sess)