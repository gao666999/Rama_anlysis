import json

def get_list(filename):
    with open (filename,'r') as file:
        result_list = file.read()
        result_list = json.loads(result_list)
        length = len(result_list)
    return result_list,length

def sort_section(list_or):
    list_new = sorted(list_or)
    l = len(list_new)
    a = l-1
    big = list_new[a]
    small = list_new[0]
    section =( big - small)/20
    #print list_new
    print big,small
    print section
    u1 = str(list_new[0]) + '~' + str(list_new[0] + section)
    u2 = str(list_new[0] + section) + '~' + str(list_new[0] + 2 * section)
    u3 = str(list_new[0] + 2 * section) + '~' + str(list_new[0] + 3 * section)
    u4 = str(list_new[0] + 3 * section) + '~' + str(list_new[0] + 4 * section)
    u5 = str(list_new[0] + 4 * section) + '~' + str(list_new[0] + 5 * section)
    u6 = str(list_new[0] + 5 * section) + '~' + str(list_new[0] + 6 * section)
    u7 = str(list_new[0] + 6 * section) + '~' + str(list_new[0] + 7 * section)
    u8 = str(list_new[0] + 7 * section) + '~' + str(list_new[0] + 8 * section)
    u9 = str(list_new[0] + 8 * section) + '~' + str(list_new[0] + 9 * section)
    u10 = str(list_new[0] + 9 * section) + '~' + str(list_new[0] + 10 * section)
    u11 = str(list_new[0] + 10 * section) + '~' + str(list_new[0] + 11 * section)
    u12 = str(list_new[0] + 11 * section) + '~' + str(list_new[0] + 12 * section)
    u13 = str(list_new[0] + 12 * section) + '~' + str(list_new[0] + 13 * section)
    u14 = str(list_new[0] + 13 * section) + '~' + str(list_new[0] + 14 * section)
    u15 = str(list_new[0] + 14 * section) + '~' + str(list_new[0] + 15 * section)
    u16 = str(list_new[0] + 15 * section) + '~' + str(list_new[0] + 16 * section)
    u17 = str(list_new[0] + 16 * section) + '~' + str(list_new[0] + 17 * section)
    u18 = str(list_new[0] + 17 * section) + '~' + str(list_new[0] + 18 * section)
    u19 = str(list_new[0] + 18 * section) + '~' + str(list_new[0] + 19 * section)
    u20 = str(list_new[0] + 19 * section) + '~' + str(big)
    my_dict = {u1:0,u2:0,u3:0,u4:0,u5:0,u6:0,u7:0,u8:0,u9:0,u10:0,u11:0,u12:0,u13:0,u14:0,u15:0,u16:0,u17:0,u18:0,u19:0,u20:0}
    for i in range(0, l):
        if(list_new[0] <= list_new[i] < list_new[0] + section):
            my_dict[u1] += 1
        if(list_new[0]  + section <= list_new[i] < list_new[0] + 2 * section):
            my_dict[u2] += 1
        if(list_new[0] + 2 * section <= list_new[i] < list_new[0] +3 *  section):
            my_dict[u3] += 1
        if(list_new[0] + 3 * section <= list_new[i] < list_new[0] +4 *  section):
            my_dict[u4] += 1
        if(list_new[0] + 4 * section <= list_new[i] < list_new[0] +5 *  section):
            my_dict[u5] += 1
        if(list_new[0] + 5 * section <= list_new[i] < list_new[0] +6 *  section):
            my_dict[u6] += 1
        if(list_new[0] + 6 * section <= list_new[i] < list_new[0] +7 *  section):
            my_dict[u7] += 1
        if(list_new[0] + 7 * section <= list_new[i] < list_new[0] +8 *  section):
            my_dict[u8] += 1
        if(list_new[0] + 8 * section <= list_new[i] < list_new[0] +9 *  section):
            my_dict[u9] += 1
        if(list_new[0] + 9 * section <= list_new[i] < list_new[0] +10 *  section):
            my_dict[u10] += 1
        if(list_new[0] + 10 * section <= list_new[i] < list_new[0] +11 *  section):
            my_dict[u11] += 1
        if(list_new[0] + 11 * section <= list_new[i] < list_new[0] +12 *  section):
            my_dict[u12] += 1
        if(list_new[0] + 12 * section <= list_new[i] < list_new[0] +13 *  section):
            my_dict[u13] += 1
        if(list_new[0] + 13 * section <= list_new[i] < list_new[0] +14 *  section):
            my_dict[u14] += 1
        if(list_new[0] + 14 * section <= list_new[i] < list_new[0] +15 *  section):
            my_dict[u15] += 1
        if(list_new[0] + 15 * section <= list_new[i] < list_new[0] +16 *  section):
            my_dict[u16] += 1
        if(list_new[0] + 16 * section <= list_new[i] < list_new[0] +17 *  section):
            my_dict[u17] += 1
        if(list_new[0] + 17 * section <= list_new[i] < list_new[0] +18 *  section):
            my_dict[u18] += 1
        if(list_new[0] + 18 * section <= list_new[i] < list_new[0] +19 *  section):
            my_dict[u19] += 1
        if(list_new[0] + 19 * section <= list_new[i] <=list_new[a]):
            my_dict[u20] += 1
    return my_dict
if __name__ =='__main__':
    filename = '/Users/xg666/Desktop/getTER/result/save_distance.txt'
    distance_list,length = get_list(filename)
    result = sort_section(distance_list)
    print result
