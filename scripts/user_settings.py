machines = [
	{
		'name': 'user1',
		'mach': 'i686',
		'workdir': 'i686-workdir', # created on the master
		'hostdir': '/hostdir',  # must exist on the slave
		'crosstarget': 'native',
		'slave_name': 'i686_void',
		'slave_pass': 'SLAVE_PASSWORD',
		'admin': 'user1'
	},
	{
		'name': 'user2',
		'mach': 'x86_64',
		'workdir': 'x86_64-workdir', # created on the master
		'hostdir': '/hostdir', # must exist on slave
		'crosstarget': 'native',
		'slave_name': 'x86_64_void',
		'slave_pass': 'SLAVE_PASSWORD',
		'admin': 'user2'
	}
	{
		'name': 'user3',
		'mach': 'armv6l',
		'workdir': 'cross-rpi-workdir', # created on the master
		'hostdir': '/hostdir', # must exist on slave
		'crosstarget': 'armv6hf',
		'slave_name': 'crossrpi_void',
		'slave_pass': 'SLAVE_PASSWORD',
		'admin': 'user3'
	}
]

web_users = [('user1', 'USER_PASSWORD'), ('user2', 'USER_PASSWORD')]
