from keyword_encode import encode_keywords
import ray

ray.init(object_store_memory=100 * 1000000,
         redis_max_memory=100 * 1000000)

encode_keywords(csv_path='example/output.csv',
                out_path='example/encodedStories.txt',
                title_field='storytitle',
                body_field='Story',
                keyword_gen='Story')  