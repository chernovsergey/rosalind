import math

s = "483 1111 99 186 128 355 1480 811 1064 1296 468 370 425 129 899 771 1239 184 908 441 572 911 256 799 981 938 0 227 997 553 1239 101 682 939 983 795 156 810 569 312 1125 1281 1294 227 541 1223 570 369 1381 230 709 685 542 128 314 1040 386 1166 936 1165 241 1351 782 1012 756 1211 910 1367 927 369 1110 199 1037 416 1324 1094 413 643 257 312 798 884 1039 884 1111 269 1250 581 340 113 1253 1012 71 596 128 1168 669 1379 1140 544 724 700 1409 1168 355 912 698 499 128 813 1352 670 1352 440 568 1224 1352 1367 113 443 667 1125 1253 1067 1352 681 780 497 241 596 315 1055 468 837"
spectr = sorted(map(int, s.split(" ")))
out = {}

for i in spectr:
	for j in spectr:
		if  i-j != 0:
			out[int(math.fabs(i-j))] = out.get(int(math.fabs(i-j)),0) + 1


res = {}
for i in out:
	res[out[i]] = res.get(out[i],[]) + [i]

M = 20
for i in sorted(res)[::-1]:
	for j in sorted(res[i])[::-1]:

		print j,