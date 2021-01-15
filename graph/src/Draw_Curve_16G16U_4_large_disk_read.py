import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


benchmark1 = "Benchmark: Hadoop Kmeans"
# benchmark2 = "Benchmark: Hadoop WordCount"
# WordCount 18G18U CPU_overall
# t1 = ""
# time1 = ""  
# benchmark1_a1 = ""
# benchmark1_b1 = ""
# benchmark1_c1 = ""
# benchmark1_d1 = ""

num = 13
workers = 4

t1 = "Hadoop TeraSort"  
time1 = "27"
benchmark1_a1 = ""  
benchmark1_b1 = ""
benchmark1_c1 = "1548726660000,0.0,18841.6,0.0,3.6 1548726665000,0.0,97484.8,0.0,1.6 1548726670000,0.0,720076.8,0.0,31.6 1548726675000,0.0,28735897.6,0.0,100.0 1548726680000,0.0,240360652.8,0.0,523.0 1548726685000,0.0,445137715.2,0.0,914.0 1548726690000,0.0,73986048.0,0.0,152.4"
benchmark1_d1 = ""

t2 = "Spark TeraSort"
time2 = "31"  
benchmark2_a1 = ""  
benchmark2_b1 = ""
benchmark2_c1 = "1548726660000,0.0,18841.6,0.0,3.6 1548726665000,0.0,97484.8,0.0,1.6 1548726670000,0.0,720076.8,0.0,31.6 1548726675000,0.0,28735897.6,0.0,100.0 1548726680000,0.0,240360652.8,0.0,523.0 1548726685000,0.0,445137715.2,0.0,914.0 1548726690000,0.0,73986048.0,0.0,152.4"
benchmark2_d1 = ""

t3 = "Hadoop Bayes"
time3 = "27"
benchmark3_a1 = ""  
benchmark3_b1 = ""
benchmark3_c1 = "1548726920000,0.0,125381017.6,0.0,261.2 1548726925000,0.0,232629862.4,0.0,489.2 1548726930000,1638.4,126038016.0,0.4,258.4 1548726935000,0.0,23779737.6,0.0,56.8 1548726940000,0.0,45657292.8,0.0,95.8 1548726945000,0.0,42934272.0,0.0,124.0 1548726950000,0.0,221000499.2,0.0,501.6 1548726955000,0.0,343812505.6,0.0,713.0"
benchmark3_d1 = ""

t4 = "Spark WordCount"
time4 = "30"
benchmark4_a1 = ""  
benchmark4_b1 = ""
benchmark4_c1 = "1548726920000,0.0,125381017.6,0.0,261.2 1548726925000,0.0,232629862.4,0.0,489.2 1548726930000,1638.4,126038016.0,0.4,258.4 1548726935000,0.0,23779737.6,0.0,56.8 1548726940000,0.0,45657292.8,0.0,95.8 1548726945000,0.0,42934272.0,0.0,124.0 1548726950000,0.0,221000499.2,0.0,501.6 1548726955000,0.0,343812505.6,0.0,713.0"
benchmark4_d1 = ""

t5 = "Hadoop PageRank"
time5 = "48"
benchmark5_a1 = ""  
benchmark5_b1 = ""
benchmark5_c1 = "1548727105000,0.0,40960.0,0.0,1.0 1548727110000,0.0,10751180.8,0.0,34.0 1548727115000,0.0,122880.0,0.0,8.2 1548727120000,0.0,9446195.2,0.0,39.4 1548727125000,0.0,10895360.0,0.0,34.6 1548727130000,0.0,17344102.4,0.0,62.8 1548727135000,0.0,25324748.8,0.0,80.8 1548727140000,0.0,11625267.2,0.0,37.2 1548727145000,0.0,1428684.8,0.0,11.4 1548727150000,0.0,28672.0,0.0,0.8 1548727155000,0.0,8565555.2,0.0,26.8 1548727160000,0.0,31737446.4,0.0,88.4 1548727165000,0.0,19933593.6,0.0,59.6 1548727170000,0.0,4687462.4,0.0,15.0"
benchmark5_d1 = ""

t6 = "Spark PageRank"
time6 = "33"
benchmark6_a1 = ""  
benchmark6_b1 = ""
benchmark6_c1 = "1548727105000,0.0,40960.0,0.0,1.0 1548727110000,0.0,10751180.8,0.0,34.0 1548727115000,0.0,122880.0,0.0,8.2 1548727120000,0.0,9446195.2,0.0,39.4 1548727125000,0.0,10895360.0,0.0,34.6 1548727130000,0.0,17344102.4,0.0,62.8 1548727135000,0.0,25324748.8,0.0,80.8 1548727140000,0.0,11625267.2,0.0,37.2 1548727145000,0.0,1428684.8,0.0,11.4 1548727150000,0.0,28672.0,0.0,0.8 1548727155000,0.0,8565555.2,0.0,26.8 1548727160000,0.0,31737446.4,0.0,88.4 1548727165000,0.0,19933593.6,0.0,59.6 1548727170000,0.0,4687462.4,0.0,15.0"
benchmark6_d1 = ""

t7 = "Hadoop Bayes"
time7 = "268"
benchmark7_a1 = ""
benchmark7_b1 = ""
benchmark7_c1 = "1548727505000,0.0,13926.4,0.0,0.8 1548727510000,0.0,156467.2,0.0,11.4 1548727515000,0.0,11970150.4,0.0,44.2 1548727520000,0.0,3878092.8,0.0,26.8 1548727525000,0.0,61383475.2,0.0,155.0"
benchmark7_d1 = ""

t8 = "Spark Bayes"
time8 = "44"
benchmark8_a1 = ""
benchmark8_b1 = ""
benchmark8_c1 = "1548727505000,0.0,13926.4,0.0,0.8 1548727510000,0.0,156467.2,0.0,11.4 1548727515000,0.0,11970150.4,0.0,44.2 1548727520000,0.0,3878092.8,0.0,26.8 1548727525000,0.0,61383475.2,0.0,155.0"
benchmark8_d1 = ""

t9 = "Hadoop Kmeans"
time9 = "126"
benchmark9_a1 = ""  
benchmark9_b1 = ""
benchmark9_c1 = "1548728180000,0.0,3276.8,0.0,0.8 1548728185000,0.0,42598.4,0.0,1.6 1548728190000,0.0,13926.4,0.0,1.4 1548728195000,0.0,130252.8,0.0,7.6 1548728200000,0.0,166297.6,0.0,15.4 1548728205000,0.0,75366.4,0.0,8.4 1548728210000,0.0,23756.8,0.0,4.2 1548728215000,0.0,12288.0,0.0,0.8 1548728220000,0.0,7372.8,0.0,1.2 1548728225000,0.0,26214.4,0.0,2.8 1548728230000,0.0,43417.6,0.0,5.6 1548728235000,819.2,37683.2,0.2,5.0 1548728240000,0.0,40140.8,0.0,5.2 1548728245000,0.0,0.0,0.0,0.0 1548728250000,0.0,7372.8,0.0,0.6 1548728255000,0.0,12288.0,0.0,1.6 1548728260000,0.0,16384.0,0.0,2.2 1548728265000,0.0,14745.6,0.0,2.2 1548728270000,0.0,13926.4,0.0,3.0 1548728275000,0.0,20480.0,0.0,3.6 1548728280000,0.0,7372.8,0.0,1.6 1548728285000,0.0,8192.0,0.0,0.8 1548728290000,0.0,21299.2,0.0,2.0 1548728295000,0.0,9011.2,0.0,1.2 1548728300000,0.0,23756.8,0.0,1.2 1548728305000,0.0,12288.0,0.0,2.2 1548728310000,0.0,19660.8,0.0,2.2 1548728315000,0.0,5734.4,0.0,0.8 1548728320000,0.0,12288.0,0.0,1.4 1548728325000,0.0,12288.0,0.0,1.6 1548728330000,0.0,24576.0,0.0,3.8 1548728335000,0.0,2457.6,0.0,0.4 1548728340000,0.0,0.0,0.0,0.0 1548728345000,0.0,4915.2,0.0,0.8 1548728350000,0.0,11468.8,0.0,1.6 1548728355000,0.0,11468.8,0.0,1.6 1548728360000,0.0,11468.8,0.0,2.0 1548728365000,0.0,3276.8,0.0,0.6 1548728370000,0.0,2457.6,0.0,0.4 1548728375000,0.0,6553.6,0.0,0.8 1548728380000,0.0,10649.6,0.0,1.2 1548728385000,0.0,16384.0,0.0,2.2 1548728390000,0.0,4915.2,0.0,0.8 1548728395000,0.0,4915.2,0.0,0.8 1548728400000,0.0,819.2,0.0,0.2 1548728405000,0.0,9830.4,0.0,1.4 1548728410000,0.0,9830.4,0.0,1.0 1548728415000,0.0,20480.0,0.0,1.6 1548728420000,0.0,25395.2,0.0,1.2 1548728425000,0.0,21299.2,0.0,3.2 1548728430000,0.0,13107.2,0.0,0.4 1548728435000,0.0,25888358.4,0.0,62.4 1548728440000,0.0,16797696.0,0.0,40.8 1548728445000,819.2,10754457.6,0.2,27.4 1548728450000,0.0,40140.8,0.0,1.6 1548728455000,0.0,5734.4,0.0,0.8 1548728460000,0.0,7033651.2,0.0,35.8 1548728465000,0.0,3910860.8,0.0,14.6 1548728470000,0.0,153190.4,0.0,13.6 1548728475000,0.0,107315.2,0.0,8.8 1548728480000,0.0,36044.8,0.0,5.0 1548728485000,0.0,8192.0,0.0,1.2 1548728490000,0.0,27033.6,0.0,1.4 1548728495000,0.0,49152.0,0.0,4.8 1548728500000,0.0,29491.2,0.0,4.0 1548728505000,0.0,23756.8,0.0,2.0 1548728510000,0.0,12288.0,0.0,1.6 1548728515000,0.0,8192.0,0.0,0.8 1548728520000,0.0,35225.6,0.0,2.4 1548728525000,0.0,26214.4,0.0,2.4 1548728530000,0.0,22118.4,0.0,2.0 1548728535000,0.0,14745.6,0.0,1.4 1548728540000,0.0,40960.0,0.0,3.6 1548728545000,0.0,23756.8,0.0,1.6 1548728550000,0.0,38502.4,0.0,2.2 1548728555000,0.0,25395.2,0.0,2.6 1548728560000,0.0,4096.0,0.0,0.4 1548728565000,0.0,31129.6,0.0,4.6 1548728570000,0.0,38502.4,0.0,3.6 1548728575000,0.0,302284.8,0.0,3.2 1548728580000,0.0,59645132.8,0.0,130.0 1548728585000,0.0,27971584.0,0.0,60.0 1548728590000,0.0,58176307.2,0.0,120.4 1548728595000,0.0,38502.4,0.0,1.6 1548728600000,0.0,61566156.8,0.0,135.2 1548728605000,0.0,203575296.0,0.0,422.0 1548728610000,0.0,271621324.8,0.0,555.8 1548728615000,0.0,333699481.6,0.0,686.0 1548728620000,0.0,324341760.0,0.0,664.0"
benchmark9_d1 = ""

t10 = "Spark Kmeans"
time10 = "34"
benchmark10_a1 = ""  
benchmark10_b1 = ""
benchmark10_c1 = "1548728180000,0.0,3276.8,0.0,0.8 1548728185000,0.0,42598.4,0.0,1.6 1548728190000,0.0,13926.4,0.0,1.4 1548728195000,0.0,130252.8,0.0,7.6 1548728200000,0.0,166297.6,0.0,15.4 1548728205000,0.0,75366.4,0.0,8.4 1548728210000,0.0,23756.8,0.0,4.2 1548728215000,0.0,12288.0,0.0,0.8 1548728220000,0.0,7372.8,0.0,1.2 1548728225000,0.0,26214.4,0.0,2.8 1548728230000,0.0,43417.6,0.0,5.6 1548728235000,819.2,37683.2,0.2,5.0 1548728240000,0.0,40140.8,0.0,5.2 1548728245000,0.0,0.0,0.0,0.0 1548728250000,0.0,7372.8,0.0,0.6 1548728255000,0.0,12288.0,0.0,1.6 1548728260000,0.0,16384.0,0.0,2.2 1548728265000,0.0,14745.6,0.0,2.2 1548728270000,0.0,13926.4,0.0,3.0 1548728275000,0.0,20480.0,0.0,3.6 1548728280000,0.0,7372.8,0.0,1.6 1548728285000,0.0,8192.0,0.0,0.8 1548728290000,0.0,21299.2,0.0,2.0 1548728295000,0.0,9011.2,0.0,1.2 1548728300000,0.0,23756.8,0.0,1.2 1548728305000,0.0,12288.0,0.0,2.2 1548728310000,0.0,19660.8,0.0,2.2 1548728315000,0.0,5734.4,0.0,0.8 1548728320000,0.0,12288.0,0.0,1.4 1548728325000,0.0,12288.0,0.0,1.6 1548728330000,0.0,24576.0,0.0,3.8 1548728335000,0.0,2457.6,0.0,0.4 1548728340000,0.0,0.0,0.0,0.0 1548728345000,0.0,4915.2,0.0,0.8 1548728350000,0.0,11468.8,0.0,1.6 1548728355000,0.0,11468.8,0.0,1.6 1548728360000,0.0,11468.8,0.0,2.0 1548728365000,0.0,3276.8,0.0,0.6 1548728370000,0.0,2457.6,0.0,0.4 1548728375000,0.0,6553.6,0.0,0.8 1548728380000,0.0,10649.6,0.0,1.2 1548728385000,0.0,16384.0,0.0,2.2 1548728390000,0.0,4915.2,0.0,0.8 1548728395000,0.0,4915.2,0.0,0.8 1548728400000,0.0,819.2,0.0,0.2 1548728405000,0.0,9830.4,0.0,1.4 1548728410000,0.0,9830.4,0.0,1.0 1548728415000,0.0,20480.0,0.0,1.6 1548728420000,0.0,25395.2,0.0,1.2 1548728425000,0.0,21299.2,0.0,3.2 1548728430000,0.0,13107.2,0.0,0.4 1548728435000,0.0,25888358.4,0.0,62.4 1548728440000,0.0,16797696.0,0.0,40.8 1548728445000,819.2,10754457.6,0.2,27.4 1548728450000,0.0,40140.8,0.0,1.6 1548728455000,0.0,5734.4,0.0,0.8 1548728460000,0.0,7033651.2,0.0,35.8 1548728465000,0.0,3910860.8,0.0,14.6 1548728470000,0.0,153190.4,0.0,13.6 1548728475000,0.0,107315.2,0.0,8.8 1548728480000,0.0,36044.8,0.0,5.0 1548728485000,0.0,8192.0,0.0,1.2 1548728490000,0.0,27033.6,0.0,1.4 1548728495000,0.0,49152.0,0.0,4.8 1548728500000,0.0,29491.2,0.0,4.0 1548728505000,0.0,23756.8,0.0,2.0 1548728510000,0.0,12288.0,0.0,1.6 1548728515000,0.0,8192.0,0.0,0.8 1548728520000,0.0,35225.6,0.0,2.4 1548728525000,0.0,26214.4,0.0,2.4 1548728530000,0.0,22118.4,0.0,2.0 1548728535000,0.0,14745.6,0.0,1.4 1548728540000,0.0,40960.0,0.0,3.6 1548728545000,0.0,23756.8,0.0,1.6 1548728550000,0.0,38502.4,0.0,2.2 1548728555000,0.0,25395.2,0.0,2.6 1548728560000,0.0,4096.0,0.0,0.4 1548728565000,0.0,31129.6,0.0,4.6 1548728570000,0.0,38502.4,0.0,3.6 1548728575000,0.0,302284.8,0.0,3.2 1548728580000,0.0,59645132.8,0.0,130.0 1548728585000,0.0,27971584.0,0.0,60.0 1548728590000,0.0,58176307.2,0.0,120.4 1548728595000,0.0,38502.4,0.0,1.6 1548728600000,0.0,61566156.8,0.0,135.2 1548728605000,0.0,203575296.0,0.0,422.0 1548728610000,0.0,271621324.8,0.0,555.8 1548728615000,0.0,333699481.6,0.0,686.0 1548728620000,0.0,324341760.0,0.0,664.0"
benchmark10_d1 = ""

t11 = "Spark LDA"
time11 = "34"
benchmark11_a1 = ""  
benchmark11_b1 = ""
benchmark11_c1 = "1548743645000,0.0,35225.6,0.0,1.2 1548743650000,0.0,175308.8,0.0,19.6 1548743655000,0.0,58159923.2,0.0,142.4 1548743660000,0.0,23745331.2,0.0,56.2 1548743665000,0.0,13289881.6,0.0,28.4 1548743670000,0.0,62893260.8,0.0,129.6"
benchmark11_d1 = ""

t12 = "Spark PCA"
time12 = "38"
benchmark12_a1 = ""  
benchmark12_b1 = ""
benchmark12_c1 = "1548743395000,0.0,15564.8,0.0,1.4 1548743400000,0.0,18841.6,0.0,2.8 1548743405000,0.0,44378521.6,0.0,98.2 1548743410000,819.2,101998592.0,0.2,212.0 1548743415000,0.0,15862169.6,0.0,34.0"
benchmark12_d1 = ""

t13 = "Spark LR"
time13 = "41"
benchmark13_a1 = ""  
benchmark13_b1 = ""
benchmark13_c1 = "1548742825000,0.0,31612108.8,0.0,65.4 1548742830000,0.0,33414348.8,0.0,74.0 1548742835000,0.0,47886336.0,0.0,109.2 1548742840000,397312.0,43279155.2,2.0,93.0 1548742845000,1592524.8,49487052.8,6.0,103.2 1548742850000,483328.0,30922342.4,3.6,64.4 1548742855000,1851392.0,92029747.2,12.4,190.2 1548742860000,143360.0,33362739.2,0.8,69.8 1548742865000,819.2,51879116.8,0.2,108.4 1548742870000,819.2,192768409.6,0.2,480.4 1548742875000,5734.4,385045299.2,1.4,869.4 1548742880000,2457.6,425701376.0,0.6,874.8 1548742885000,3276.8,413265920.0,0.8,844.2 1548742890000,4096.0,422956236.8,1.0,869.8 1548742895000,3276.8,438785638.4,0.8,904.8 1548742900000,4096.0,379452620.8,1.0,778.6 1548742905000,4096.0,420457676.8,1.0,855.0 1548742910000,2457.6,316400435.2,0.6,644.8"
benchmark13_d1 = ""

t14 = "Spark LDA"
time14 = "54"
benchmark14_a1 = ""  
benchmark14_b1 = ""
benchmark14_c1 = ""
benchmark14_d1 = ""

t15 = "Spark SVM"
time15 = "40"
benchmark15_a1 = ""
benchmark15_b1 = ""
benchmark15_c1 = ""
benchmark15_d1 = ""

col_labels = []
row_labels = ['CPU mean(%)', 'CPU standard deviation(%)', 'RAM mean(%)', 'RAM standard deviation(%)', 'Disk read mean(Mbps)', 'Disk read standard deviation(Mbps)', \
              'Disk write mean(%)', 'Disk write standard deviation(Mbps)', 'Network receive mean(Mbps)', 'Network receive standard deviation(Mbps)', \
              'Network send mean(Mbps)', 'Network send standard deviation(Mbps)']
table_vals = []
col_value = []
mean_value = []
row_colors = ['gold']
for i in range(1,num+1):
    c = locals()['benchmark%s_c1' % str(i)].split(" ")
    x = []
    y_c1 = []
    y_c2 = []
    l = 0  
    for n in c:   
        l = l + 1        
        m = n.split(",")
        x.append(5*int(l))          
        y_c1.append(float('%.2f' % (float(m[1]))) / 1024 / 1024 / workers)
        y_c2.append(float('%.2f' % (float(m[2]))) / 1024 / 1024 / workers)
    print("Disk read mean: %sMbps" % ('%.2f' % (np.mean(np.array(y_c1)))))
    print("Disk read standard deviation: %sMbps" % ('%.2f' % (np.std(np.array(y_c1)))))
    print("Disk write mean: %sMbps" % ('%.2f' % (np.mean(np.array(y_c2)))))
    print("Disk write standard deviation: %sMbps" % ('%.2f' % (np.std(np.array(y_c2)))))
#     col_value_float.append(('%.2f' % (np.mean(np.array(y_a))))) 
#     col_value_float.append(('%.2f' % (np.std(np.array(y_a)))))
#     col_value_float.append(('%.2f' % (np.mean(np.array(y_b))))) 
#     col_value_float.append(('%.2f' % (np.std(np.array(y_b)))))
#     col_value_float.append(('%.2f' % (np.mean(np.array(y_c1)))))
#     col_value_float.append(('%.2f' % (np.std(np.array(y_c1))))) 
#     col_value_float.append(('%.2f' % (np.mean(np.array(y_c2))))) 
#     col_value_float.append(('%.2f' % (np.std(np.array(y_c2))))) 
#     col_value_float.append(('%.2f' % (np.mean(np.array(y_d1))))) 
#     col_value_float.append(('%.2f' % (np.std(np.array(y_d1))))) 
#     col_value_float.append(('%.2f' % (np.mean(np.array(y_d2))))) 
#     col_value_float.append(('%.2f' % (np.std(np.array(y_d2)))))
    mean_value.append([('%.2f' % (np.mean(np.array(y_c1)))), ('%.2f' % (np.mean(np.array(y_c2))))])
    

table_vals = []
tmp = []
for col in mean_value:
    print(np.array(col))
# for col in col_value:
#     print(np.array(col))
# for i in range(0,len(col_value[0])):
#     for col in col_value:
#         tmp.append(col[i])
#     table_vals.append(tmp)
# #     print(tmp)
#     tmp = []
# print(table_vals)
# print(col_labels)
# print(row_labels)
# my_table = plt.table(cellText=table_vals, colWidths=[0.2]*num, \
#                      rowLabels=row_labels, colLabels=col_labels, \
#                      loc='best')
# my_table.set_fontsize(20)
# plt.axis('off')

# plt.show()