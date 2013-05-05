machines = [
	{
		'name': 'user1',
		'mach': 'i686',
		'http_git_url': 'https://github.com/xtraeme/xbps-packages',
		'workdir': 'i686-workdir', # created on the master
		'hostdir': '/hostdir',  # must exist on the slave
		'slave_name': 'i686_void',
		'slave_pass': 'SLAVE_PASSWORD',
		'admin': 'user1'
	},
	{
		'name': 'user2',
		'mach': 'x86_64',
		'http_git_url': 'https://github.com/xtraeme/xbps-packages',
		'workdir': 'x86_64-workdir', # created on the master
		'hostdir': '/hostdir', # must exist on slave
		'slave_name': 'x86_64_void',
		'slave_pass': 'SLAVE_PASSWORD',
		'admin': 'user2'
	}
]

web_users = [('user1', 'USER_PASSWORD'), ('user2', 'USER_PASSWORD')]
