#to encode a csv file such that it can be used to train a model/ To generate keywords for a csv file
from keyword_encode import encode_keywords
import ray

ray.init(object_store_memory=100 * 1000000,
         redis_max_memory=100 * 1000000)

#Reference: https://github.com/minimaxir/gpt-2-keyword-generation/tree/master/example (Official Example of Keyword Generation)
#OR
#https://github.com/minimaxir/gpt-2-keyword-generation (Taxonomy, Usage) - explains various parameters of encode_keyword()
#OR
#https://github.com/minimaxir/gpt-2-keyword-generation/blob/master/keyword_encode.py (Line 25)(encode_keywords function) - Displays all parameters and their default values for encode_keywords()

encode_keywords(csv_path='example/ROCStories.csv',#path to input csv file
                out_path='example/encodedStories.txt',#path for output file (must be .txt)
                title_field='storytitle',#column name for title column (optional)
                body_field='Story',#column name for column with large amount of text depending on title field(optional)
                keyword_gen='Story'#column name from which text keywords should be generated
                #there are also category_field for category column if present | and keywords_field for a column filled with keywords for each field in keyword_gen column - if you don't want the model to extract keywords by itself 
                )  