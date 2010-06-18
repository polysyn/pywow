# -*- coding: utf-8 -*-
"""
`builds' is a dict lookup on build to a tuple
(patch, expansion)
patch is a version string, expansion is an int:
 * 0: vanilla
 * 1: TBC
 * 2: WotLK
 * 3: Cataclysm
"""

builds = {
	12232: ("4.0.0", 3),
	12166: ("3.3.5", 2),
	12164: ("4.0.0", 3),
	12148: ("3.3.5", 2),
	12124: ("3.3.5", 2),
	12122: ("4.0.0", 3),
	12065: ("4.0.0", 3),
	12045: ("3.3.5", 2),
	12025: ("4.0.0", 3),
	11993: ("3.3.5", 2), # 3.0.5 PTR
	11927: ("4.0.0", 3), # Alpha F&F
	11723: ("3.3.3", 2),
	11685: ("3.3.3", 2),
	11599: ("3.3.2", 2),
	11403: ("3.3.2", 2),
	11159: ("3.3.0", 2),
	10958: ("3.3.0", 2),
	10952: ("3.3.0", 2),
	10894: ("3.3.0", 2),
	10835: ("3.3.0", 2),
	10805: ("3.3.0", 2),
	10772: ("3.3.0", 2),
	10747: ("3.3.0", 2),
	10712: ("3.3.0", 2),
	10676: ("3.3.0", 2),
	10623: ("3.3.0", 2),
	10596: ("3.3.0", 2),
	10571: ("3.3.0", 2),
	10554: ("3.3.0", 2),
	10505: ("3.2.2", 2),
	10482: ("3.2.2", 2),
	10392: ("3.2.2", 2),
	10371: ("3.2.2", 2),
	10357: ("3.2.2", 2),
	10314: ("3.2.0", 2),
	10287: ("4.0.0", 3), # Blizzcon Cataclysm preview
	10192: ("3.2.0", 2),
	10083: ("3.2.0", 2),
	10072: ("3.2.0", 2),
	10048: ("3.2.0", 2),
	10026: ("3.2.0", 2),
	9947:  ("3.1.3", 2),
	9901:  ("3.1.2", 2),
	9889:  ("3.1.2", 2),
	9868:  ("3.1.2", 2),
	9855:  ("3.1.2", 2),
	9835:  ("3.1.1", 2),
	9806:  ("3.1.1", 2),
	9767:  ("3.1.0", 2),
	9757:  ("3.1.0", 2),
	9742:  ("3.1.0", 2),
	9733:  ("3.1.0", 2),
	9722:  ("3.1.0", 2),
	9704:  ("3.1.0", 2),
	9684:  ("3.1.0", 2),
	9658:  ("3.1.0", 2),
	9637:  ("3.1.0", 2),
	9626:  ("3.1.0", 2),
	9614:  ("3.1.0", 2),
	9551:  ("3.0.9", 2),
	9506:  ("3.0.8", 2),
	9464:  ("3.0.8", 2),
	9328:  ("3.0.8", 2),
	9183:  ("3.0.3", 2),
	9095:  ("3.0.3", 2),
	9056:  ("3.0.2", 2),
	9038:  ("3.0.2", 2),
	8606:  ("2.4.3", 1),
	8478:  ("2.4.3", 1),
	8209:  ("2.4.2", 1),
	8209:  ("2.4.2", 1),
	8125:  ("2.4.1", 1),
	8089:  ("2.4.0", 1),
	8063:  ("2.4.0", 1),
	8049:  ("2.4.0", 1),
	8031:  ("2.4.0", 1),
	8016:  ("2.4.0", 1),
	7994:  ("2.4.0", 1),
	7979:  ("2.4.0", 1),
	7962:  ("2.4.0", 1),
	7958:  ("2.4.0", 1),
	7948:  ("2.4.0", 1),
	7923:  ("2.4.0", 1),
	7897:  ("2.4.0", 1),
	7799:  ("2.3.3", 1),
	7741:  ("2.3.2", 1),
	7720:  ("2.3.2", 1),
	7705:  ("2.3.2", 1),
	7677:  ("2.3.2", 1),
	7655:  ("2.3.2", 1),
	7627:  ("2.3.2", 1),
	7359:  ("2.2.3", 1),
	7344:  ("2.2.3", 1),
	7318:  ("2.2.2", 1),
	7304:  ("2.2.2", 1),
	7286:  ("2.2.2", 1),
	7272:  ("2.2.0", 1),
	7261:  ("2.2.0", 1),
	7250:  ("2.2.0", 1),
	7229:  ("2.2.0", 1),
	7214:  ("2.2.0", 1),
	7195:  ("2.2.0", 1),
	7189:  ("2.2.0", 1),
	7187:  ("2.2.0", 1),
	7175:  ("2.2.0", 1),
	7153:  ("2.2.0", 1),
	7125:  ("2.2.0", 1),
	7091:  ("2.2.0", 1),
	7051:  ("2.2.0", 1),
	6983:  ("2.2.0", 1),
	6932:  ("2.2.0", 1),
	6898:  ("2.1.3", 1),
	6803:  ("2.1.2", 1),
	6739:  ("2.1.1", 1),
	6729:  ("2.1.1", 1),
	6692:  ("2.1.0", 1),
	6678:  ("2.1.0", 1),
	6655:  ("2.1.0", 1),
	6641:  ("2.1.0", 1),
	6624:  ("2.1.0", 1),
	6607:  ("2.1.0", 1),
	6592:  ("2.1.0", 1),
	6577:  ("2.1.0", 1),
	6337:  ("2.0.6", 1),
	60??:  ("2.0.0", 1),
	6320:  ("2.0.5", 1),
	6314:  ("2.0.4", 1),
	6299:  ("2.0.3", 1),
	6180:  ("2.0.1", 1),
	6175:  ("2.0.1", 1),
	6157:  ("2.0.1", 1),
	6144:  ("2.0.2", 1),
	6114:  ("2.0.1", 1),
	6108:  ("2.0.2", 1),
	6082:  ("2.0.1", 1),
	6052:  ("2.0.0", 1),
	6046:  ("2.0.0", 1),
	6022:  ("2.0.0", 1),
	5991:  ("2.0.0", 1),
	5965:  ("2.0.0", 1),
	5921:  ("2.0.0", 1),
	5894:  ("2.0.0", 1),
	5849:  ("2.0.0", 1),
	5666:  ("2.0.0", 1),
	5665:  ("2.0.0", 1),
	5610:  ("2.0.0", 1),
	6005:  ("1.12.2", 0),
	5875:  ("1.12.1", 0),
	5875:  ("1.12.1", 0),
	5803:  ("1.12.1", 0),
	5734:  ("1.12.1", 0),
	5595:  ("1.12.0", 0),
	5595:  ("1.12.0", 0),
	5590:  ("1.12.0", 0),
	5579:  ("1.12.0", 0),
	5561:  ("1.12.0", 0),
	5537:  ("1.12.0", 0),
	5521:  ("1.12.0", 0),
	5496:  ("1.12.0", 0),
	5464:  ("1.11.2", 0),
	5462:  ("1.11.1", 0),
	5428:  ("1.11.0", 0),
	5413:  ("1.11.0", 0),
	5383:  ("1.11.0", 0),
	5366:  ("1.11.0", 0),
	5344:  ("1.11.0", 0),
	5302:  ("1.10.2", 0),
	5230:  ("1.10.1", 0),
	5195:  ("1.10.0", 0),
	5086:  ("1.9.4", 0),
	5059:  ("1.9.3", 0),
	4996:  ("1.9.2", 0),
	4983:  ("1.9.2", 0),
	4937:  ("1.9.0", 0),
	4878:  ("1.8.4", 0),
	4807:  ("1.8.3", 0),
	4784:  ("1.8.2", 0),
	4769:  ("1.8.1", 0),
	4735:  ("1.8.0", 0),
	4695:  ("1.7.1", 0),
	4671:  ("1.7.0", 0),
	4544:  ("1.6.1", 0),
	4500:  ("1.6.0", 0),
	4499:  ("1.5.1", 0),
	4442:  ("1.5.0", 0),
	4375:  ("1.4.2", 0),
	4364:  ("1.4.1", 0),
	4341:  ("1.4.0", 0),
	4297:  ("1.3.2", 0),
	4297:  ("1.3.1", 0),
	4284:  ("1.3.0", 0),
	4222:  ("1.2.4", 0),
	4211:  ("1.2.3", 0),
	4196:  ("1.2.2", 0),
	4150:  ("1.2.1", 0),
	4149:  ("1.2.0", 0),
	4125:  ("1.1.2", 0),
	4062:  ("1.1.1", 0),
	4044:  ("1.1.0", 0),
	3980:  ("1.0.0", 0),
}
