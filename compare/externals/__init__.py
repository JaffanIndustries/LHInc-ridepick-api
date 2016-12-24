import uber, lyft

def get_all_estimates(start_lat,start_lon,end_lat,end_lon, seat):
    estimate = dict()
    uber_estimate = uber.get_estimate(start_lat=start_lat,start_lon=start_lon,end_lat=end_lat,end_lon=end_lon,seat_count=seat)
    lyft_estimate = lyft.get_estimates(start_lat=start_lat,start_lon=start_lon,end_lat=end_lat,end_lon=end_lon)
    estimate['uber'] = uber_estimate
    estimate['lyft'] = lyft_estimate
    return merge_estimate(estimate)

def get_all_products(current_lat,current_lon):
    products = dict()
    uber_products = uber.get_products(current_lat=current_lat,current_lon=current_lon)
    lyft_products = lyft.get_products(current_lat=current_lat,current_lon=current_lon)
    products['uber'] = uber_products
    products['lyft'] = lyft_products
    return products

def merge_estimate(raw_estimate):
    thrift_merge = dict()
    final_merge = list()
    for key, value in raw_estimate.iteritems():
        if key == 'uber':
            for a in value:
                thrift_merge['service'] = 'uber'
                thrift_merge['product_id'] = a['product_id']
                thrift_merge['display_name'] = a['display_name']
                thrift_merge['max_cost'] = a['high_estimate']
                thrift_merge['min_cost'] = a['low_estimate']
                thrift_merge['range_estimate'] = a['estimate']
                thrift_merge['currency'] = a['currency_code']
                thrift_merge['duration'] = a['duration']
                thrift_merge['distance'] = a['distance']
                final_merge.append(thrift_merge.copy())
        elif key == 'lyft':
            for a in value:
                thrift_merge['service'] = 'lyft'
                thrift_merge['product_id'] = a['primetime_confirmation_token']
                thrift_merge['display_name'] = a['display_name']
                thrift_merge['max_cost'] = a['estimated_cost_cents_max']
                thrift_merge['min_cost'] = a['estimated_cost_cents_min']
                thrift_merge['range_estimate'] = 'null'
                thrift_merge['currency'] = a['currency']
                thrift_merge['duration'] = a['estimated_duration_seconds']
                thrift_merge['distance'] = a['estimated_distance_miles']
                final_merge.append(thrift_merge.copy())
    return final_merge