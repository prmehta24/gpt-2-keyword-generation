#to encode a csv file such that it can be used to train a model
from keyword_encode import encode_keywords
import ray

ray.init(object_store_memory=100 * 1000000,
         redis_max_memory=100 * 1000000)

encode_keywords(csv_path='example/output.csv',#path to input csv file
                out_path='example/encodedStories.txt',#path for output file
                title_field='storytitle',#column name for title column (optional)
                body_field='Story',#column name for column with large amount of text depending on title field(optional)
                keyword_gen='Story'#column name from which text keywords should be generated
                #there are also category_field for category column if present | and keywords_field for a column filled with keywords for each field in keyword_gen column - if you don't want the model to extract keywords by itself 
                )  