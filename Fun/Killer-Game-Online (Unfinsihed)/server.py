import socket
import settings
import random

def main():
	tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	tcp_server_socket.bind(settings.server)
	tcp_server_socket.listen(128)

	p1_socket, p1_addr = tcp_server_socket.accept()
	print(p1_addr)
	p2_socket, p2_addr = tcp_server_socket.accept()
	print(p2_addr)
	p3_socket, p3_addr = tcp_server_socket.accept()
	print(p3_addr)
	p4_socket, p4_addr = tcp_server_socket.accept()
	print(p4_addr)
	p5_socket, p5_addr = tcp_server_socket.accept()
	print(p5_addr)

	name = []
	role = ['Doctor', 'Police', 'Killer', 'Spy', 'Limitor']
	alive = ['Alive', 'Alive', 'Alive', 'Alive', 'Alive']
	random.shuffle(role)

	name.append(p1_socket.recv(1024).decode('utf-8'))
	name.append(p2_socket.recv(1024).decode('utf-8'))
	name.append(p3_socket.recv(1024).decode('utf-8'))
	name.append(p4_socket.recv(1024).decode('utf-8'))
	name.append(p5_socket.recv(1024).decode('utf-8'))

	name_str ='0:' + name[0] + '  ' +\
			  '1:' + name[1] + '  ' +\
			  '2:' + name[2] + '  ' +\
			  '3:' + name[3] + '  ' +\
			  '4:' + name[4]
	p1_socket.send(role[0].encode('utf-8'))
	p2_socket.send(role[1].encode('utf-8'))
	p3_socket.send(role[2].encode('utf-8'))
	p4_socket.send(role[3].encode('utf-8'))
	p5_socket.send(role[4].encode('utf-8'))

	p1_socket.send(name_str.encode('utf-8'))
	p2_socket.send(name_str.encode('utf-8'))
	p3_socket.send(name_str.encode('utf-8'))
	p4_socket.send(name_str.encode('utf-8'))
	p5_socket.send(name_str.encode('utf-8'))
	role_team = {
	'Doctor' : 'Good Guy',
	'Killer' : 'Killer',
	'Police' : 'Good Guy',
	'Spy' : 'Good Guy',
	'limitor': 'Killer'}
	q = 0
	needle = [0, 0, 0, 0, 0]
	gameRun = True
	while gameRun:
		name_str ='0:' + name[0] + ' (' + alive[0] + ')   ' +\
			  '1:' + name[1] + ' (' + alive[1] + ')   ' +\
			  '2:' + name[2] + ' (' + alive[2] + ')   ' +\
			  '3:' + name[3] + ' (' + alive[3] + ')   ' +\
			  '4:' + name[4] + ' (' + alive[4] + ')'
		while True:
			
			p1_target = p1_socket.recv(1024).decode('utf-8')
			p2_target = p2_socket.recv(1024).decode('utf-8')
			p3_target = p3_socket.recv(1024).decode('utf-8')
			p4_target = p4_socket.recv(1024).decode('utf-8')
			p5_target = p5_socket.recv(1024).decode('utf-8')

		tar = [int(p1_target), int(p2_target), int(p3_target), int(p4_target), int(p5_target)]
		limited[False, False, False, False, False]

		for i in range(5):
			if role[i] == 'Limitor' and alive[i] == 'Alive':
				limited[tar[i]] = True
				print(tar[i])
				break

		for i in range(5):
			if role[i] == 'Doctor' and alive[i] == 'Alive' and not limited[i]:
				needle[tar[i]] += 1
				if needle[tar[i]] >= 2:
					alive[tar[i]] = 'Out'
				print(tar[i])
				break

		for i in range(5):
			if role[i] == 'Police' and alive[i] == 'Alive' and not limited[i]:
				if i == 0:
					p1_socket.send(role_team[role[tar[i]]].encode('utf-8'))
				elif i == 1:
					p2_socket.send(role_team[role[tar[i]]].encode('utf-8'))
				elif i == 2:
					p3_socket.send(role_team[role[tar[i]]].encode('utf-8'))
				elif i == 3:
					p4_socket.send(role_team[role[tar[i]]].encode('utf-8'))
				elif i == 4:
					p5_socket.send(role_team[role[tar[i]]].encode('utf-8'))
				print(tar[i])
				break

		for i in range(5):
			if role[i] == 'Killer' and alive[i] == 'Alive' and not limited[i]:
				if needle[tar[i]] != 1:
					alive[tar[i]] = 'Out'
				print(tar[i])
				break

		for i in range(5):
			if role[i] == 'Spy' and alive[i] == 'Alive' and not limited[i]:
				if needle[tar[i]] != 1:
					alive[tar[i]] = 'Out'
				print(tar[i])
				break

		
		if q == 3:
			gameRun = False
	
	

	p1_socket.close()
	p2_socket.close()
	p3_socket.close()
	p4_socket.close()
	p5_socket.close()
	tcp_server_socket.close()

if __name__ == '__main__':
	main()