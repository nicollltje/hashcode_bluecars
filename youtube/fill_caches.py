from collections import Counter

def fillCaches(endpoints, max_cache_capacity):


    all_video_request = {}
    cache_size = 100
    request_list = []

    final_cache_fill = {}

    # loop over all endpoints and store all videorequests in all available caches
    for key, value in endpoints.iteritems():
        videorequests = value[0]
        bound_caches = value[1]
        for item in bound_caches:
            all_video_request[item][videorequests].append(videorequests)

    for key, valuedict in all_video_request.iteritems():
        for key2, value in valuedict.iteritems():
            count = Counter()
            count_sort = sorted(count.items(), key = lambda x: x[1], reverse=True)
            cache_capacity = 0





