from googleapiclient.discovery import build
import os

api_key = os.environ.get("youtube_api")
#api_key = 'API KEY'


def video_comments(video_id):
	# empty list for storing reply
	replies = []

	# creating youtube resource object
	youtube = build('youtube', 'v3',
					developerKey=api_key)

	# retrieve youtube video results
	video_response=youtube.commentThreads().list(
	part='snippet,replies',
	videoId=video_id
	).execute()

	# iterate video response
	while video_response:
		
		# extracting required info
		# from each result object
		for item in video_response['items']:
			
			# Extracting comments
			comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
			
			# counting number of reply of comment
			replycount = item['snippet']['totalReplyCount']

			# if reply is there
			if replycount>0:
				
				# iterate through all reply
				for reply in item['replies']['comments']:
					
					# Extract reply
					reply = reply['snippet']['textDisplay']
					
					# Store reply is list
					replies.append(reply)

			# print comment with list of reply
			print(comment, replies, end = '\n\n')

			# empty reply list
			replies = []

		# Again repeat
		if 'nextPageToken' in video_response:
			video_response = youtube.commentThreads().list(
					part = 'snippet,replies',
					videoId = video_id
				).execute()
		else:
			break

# Enter video id
#video_id = "yYuHjpZj22o"

video_list = ['v9B-FfqD0jA',
'KTBG-IME8p0',
'2iTTtD0OmvE',
'tzuBgRKb6nQ',
'kqjMQQqSm-4',
'yYuHjpZj22o',
'tt4l8AxoMzo',
'LTJ8m8cKy8g',
'IhGQVfb4L2A',
'TSyNpMq8qgk',
'oxJMwh-akgM',
'9RN6CivenCw',
'OJcwZNszt9A',
'wlWecb_xjng',
'b9NC0HBIm58',
'dcSPZwnyfaM',
'9wS3XFAyeE4',
'aWi1S0F7U10',
'Y6nmHe5yg-I',
'dd5HsvnPzio',
'mfpOyQTVhmU',
'd3U8FMGrNC0',
'JKG8m5XHuV4',
'tZGVvAgOlQk',
'poljzXm4Jew',
'IvUsBq5rSu4',
'4MUThh2x_YI',
'Kkl3fw-07V8',
'waftlloZkJI',
'TBw-QAi6xSU',
'OQ759479RRU',
'MBDPZJa9Vlw',
'vfwuboknpIc',
'H4vAdy60XNU',
'U-PVdajDRTY',
'uT05VtzbIlg',
'wmpg9nO3-lc',
'm2hizxlDAoo',
'ED0R7Ug4jF4',
'ochUtXJsGz8',
'ftMcrFwcfNc',
'ZrYZocJsSIs',
'Q4JvAhgZ2Ts',
'VUk3mOv5Npg',
'419jjGMNzJ0',
'T8m22Aru3dk',
'krr165luy2M',
'K5T94VGsu1Q',
'keV4z7MI0c0',
'933flKIg-NM',
'Hu0G4Oxbznk',
'Rnu5pNGbV8I',
'WNLIOeUDRGc',
'lqYEA2tBGus',
'NfFCC4PAg00',
'Zgfiydb6I8o',
'jpXsfhd6bEg',
'EsQPSPuwJPs',
'9q4cTPxjVks',
'CmRTFFhovmo',
'3sowN1Zrkac',
'5JdRI7cMnp8',
'yQbiYW7WWqM',
'eUscHSAJ7os',
'nWIuK09qgyY',
'JWMC_K6vfkA',
'd0qqMniGFpE',
'vM-nty_FTDc',
'scdbJ1ZBupM',
'veObtW4XG1M',
'byBhU3tKIMg',
'Y0prSGXpjFQ',
'Uq1-alDt2sw',
'T7TuB8J3BSk',
'PY76zBM08ks',
'osKBdUBVXRM',
'bVU9p6r2hQ8',
'TGi5Y9jLVlY',
'dYvrldL-9xQ',
'VLWMWIJS6CQ',
'TFtkYO16q58',
'DJwAeDAFA3Y',
'EjFgVuCGp_E',
'WHxyt9FSSCg',
'okqFqi7hm8o',
'PYzyXP-CBUU',
'k71cfmKERzg',
'StyvvMg1pV8',
'pq-u1c2jl5c',
'rGwf2ZuSbcg',
'UqbdDzfIE9M',
'btBgBRqUeyA',
'2csyWplJrO0',
'W2nz0zXcWlo',
'1_ImUspXWd4',
'pmZIDZ0jtwU',
'PdpdB195wVM',
'q4QT8PJEvpU',
'u8YLAaBqKTM',
'6uI-Ufdpr-Y',
'geVxMSkyUi8',
'3-w4tTmHbxU',
'217t4C80_is',
'2FesYM__g9U',
'gbjHjNNk2FU',
'OYxzdqZGDs0',
'0I2xODgxOfI',
'3jTL6A4lnGE',
'_GZpN9QCx9o',
'UFPbrp34lik',
'6gpgZxgTZOU',
'SmXVTX3UI7Y',
'lYdr5ajFaZ4',
'qAzCj3vmN4w',
'CSAIfCfaIZk',
'Iyyr7rMdWLU',
'p71byD00Ufw',
'4NvHhxKqoIs',
'yv-ZfCn_DO4',
'7tL2QJkfvKA',
'KuGhxuJblO8',
'VCWFjUO504I',
'_BIR9xS6tv8',
'snWfhdAZOWc',
'VS7RhFZAWgI',
'OS9X9I83-YQ',
'OThwPPNZpBE',
'CzrOyTSXdIM',
'knxIWnfZCvs',
'G1va_i1kz70',
'RvnlD8LP_3I',
'AmseBMKSIsY',
'UHcaSfrHf2Y',
'WovRQU5Y4nk',
'HlVT-F5lbI0',
'd21kuVEiCBI',
'WbSaRZE7QYg',
'nULUZcUGKMg',
'_1CS1eQwWZY',
'73xanlf5bEM',
'X20KIchhl68',
'ms1zltx1YAA',
'EMbSGEzwJlo',
'AcGUu3mV3PQ',
'4T84kXjmn-0',
'ob2JUjLpUQ0',
'p-rLVHiwu4A',
'ZXb-2epdVSc',
'iu4UAjO4MUw',
'yB2gXS5j8C8',
'Y--_Y0Gyk08',
'aa4p4VSrHt4',
'EtvoYjRQhiE',
'E1_twu4mk5E',
'gxZZDDnHbAo',
'7YlZsgU9h5c',
'vHIfwpbtfs0',
'BNtl8-2H2Qg',
'v260B1cz_ec',
'KLaXsioqyNc',
'p6mj82rBDTg',
'XEBzmgHvxGw',
'Ti86-GAsF4o',
'gxlsQclOi7A',
'auE8fDbziLM',
'WFgrPJFlgdQ',
'SZB10kXT0rg',
'pQBBsiOgMa4',
'W_pNuZ6bhs0',
'L6F1_0YXH30',
'mRRD4TQ8gRc',
'wdCgpgU9qNE',
'lh98K7S5nLI',
'eaXedrcCqzM',
'BUZyg8LGsss',
'YIXoDlD3ytI',
'ToqP8v_g4_Q',
'bBGg2wHsCeE',
'rZxDQyndAfk',
'3wTZwPCXKkM',
'uswy_E3tuv4',
'hFfi7PvVklI',
'ZSeeBnFnNY8',
'C4xjWK6nnFA',
'SWLoHdjh4vk',
'9zuKTo7UrTo',
'jhISgX5EM7E',
'bFw3vqDo4XA',
'-8qep0VXAiw',
'tce6GIsW4Tk',
'd26bJYyyCzY',
'UKGBSDdlWoc',
'f1pJLYWlDQE',
'uiPtHmt1tv8',
'HQng-1jMAKM',
'FY3Eh_L4lqw',
'RYctuzL1auY',
'kEVl73TSAJ0',
'I3yNnMOuVpY',
'GkH3xKlSBQE',
'ruuHaozCprg',
'tPW80BAaEQc',
'mBlofZ4-G6c',
'oM3i2GgCoKQ',
'Q9S4k498q5M',
'coVFXsCV4lg',
'RZvIh-X_5xE',
'XAOG56t9R4w',
'db0ihyZT-BU',
'js37haNLw4Q',
'AdITVHpDWJw',
'WlNnAFXt9dA',
'gG2RHgOwYbw',
'JdQqO2nod14',
'-AgzBCB-t9Q',
'ArNPq-ETf18',
'Wbe1ZGMHX-s',
'5fYvTM1Hq4o',
'vi5JLUAdijA',
'4liuTV7zn5E',
'PtOniQbVZCo',
'RN4RsmcGGlY',
'neX3DrfGI9c',
'aYsgp_aHQQ0',
'DFhvpRRf5CU',
'mYUA_XwLx5Q',
'-caX5xcEYjw',
'JXZX0FN9bWE',
'bCWW_OQMPgA',
'1pldqHQzoBM',
'zRfUzVmdNbA',
'jZn5BKEbih8',
'1gcoNr2O-Ok',
'TujkzyGeZ9I',
'etxd4plLRmk',
'GSfw0PbhGno',
'ZFBaoTZnafE',
'0m9D8eVyxKI',
'ghudUIPJfyI',
'lM6wAZfbCAw',
'TXRVBv6wgJQ',
'MjzK3oqId2U',
'Sn_65dhAEqE',
'bNlkIixgFOU',
'OEW5cI9wQy4',
'r3vxc7I1am8',
'8xLsXn1kQ_k',
'-Q7FenrFfT8',
'Zz0y7vrvXwo',
'RFb_AMX0-zs',
'zkcVh8N2jUQ',
'5aBT-dDUSSA',
'E64FFlsl3rA',
'86bdJc49stU',
'GG6w_vbHzY4',
'3hvD51HFJww',
'dOCx-KewTlg',
'W0Kw5afPpd8',
'Vmu2adRvwNo',
'B8JEs7CFiU0',
'wdDBNufyGG0',
'BT6W5Y7Djbg',
'9ggYL7LjrDI',
'JcV5icv_DRo',
'WcykYCEU03w',
'_r5jdsIWy44',
'H6yASwj6ixA',
'4yG1kFA_FQw',
'B587ggx92jw',
'OAM3b3oSNpM',
'hVsazxJdq4A',
'OVrFZHh9p_I',
'Y9XCpZ-zY5Y',
'cyaYEmUk-Ug',
'2bw-ip2xGeA',
'doiVWDikax8',
'N3wce7-dqgk',
'HTd0OvRvZCY',
'sbYQTiqAK2s',
'FIvilSuvZTg',
'MSNopkr4yHw',
'9dK0H9NaJaQ',
'dW0adydopx0',
'WxMfYJFhqU4',
'9gcSdJHIJIY',
'GHxXu3gv5XQ',
'c4a76LBWolY',
'DBqV6NkKteU',
'0wKCQIntVRk',
'nM4LZ0hfAy0',
'QS7EuefCM5c',
'cAqRzN44EdU',
'Mwym-eRpTvs',
'gHmoAXjaVQc',
'azXKdWXu8IY',
'73jKzI6Hnk8']


# Call function
for video_id in video_list:
	video_comments(video_id)
