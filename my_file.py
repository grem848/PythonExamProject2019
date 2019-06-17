import get_transcripts

urls = ['https://millercenter.org/the-presidency/presidential-speeches/february-5-2019-state-union-address',
        'https://millercenter.org/the-presidency/presidential-speeches/january-12-2016-2016-state-union-address',
        'https://millercenter.org/the-presidency/presidential-speeches/january-28-2008-state-union-address',
        'https://millercenter.org/the-presidency/presidential-speeches/january-27-2000-state-union-address',
        'https://millercenter.org/the-presidency/presidential-speeches/january-28-1992-state-union-address',
        'https://millercenter.org/the-presidency/presidential-speeches/january-25-1988-state-union-address',
        'https://millercenter.org/the-presidency/presidential-speeches/january-23-1980-state-union-address',
        'https://millercenter.org/the-presidency/presidential-speeches/january-30-1974-state-union-address',
        'https://millercenter.org/the-presidency/presidential-speeches/january-14-1969-state-union-address',
        'https://millercenter.org/the-presidency/presidential-speeches/january-14-1963-state-union-address']

transcripts = [get_transcripts.url_to_transcript(u) for u in urls]

print(transcripts)