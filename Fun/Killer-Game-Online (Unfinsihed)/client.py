import socket
import settings
import os
import kgol_component as kgol

def main():
	# init
	tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp_socket.connect(settings.server)
	name_data = input("输入名字：")
	tcp_socket.send(name_data.encode("utf-8"))
	print("正在等待其他玩家...")
	role = tcp_socket.recv(1024).decode("utf-8")
	player = tcp_socket.recv(1024).decode("utf-8")
	print("你本轮游戏的角色为：" + role)
	print('-' * 40)
	print(kgol.role_info[str(role)])
	print('-' * 40)
	print("本轮游戏参与的玩家")
	print(player)
	print()
	

	
	my_role = str(role)
	my_name = name_data
	gameRun = True
	
	q = 0

	# run game
	while gameRun:
		q += 1
		print("天黑请闭眼")
		print(player)
		target = input("本回合目标id(数字) > ")
		tcp_socket.send(target.encode("utf-8"))

		if my_role == 'Police':
			he_is = tcp_socket.recv(1024).decode("utf-8")
			print("Ta是 " + he_is)

		if q == 3:
			gameRun = False




	tcp_socket.close()


if __name__ == '__main__':
	main()