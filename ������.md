4.2.2键盘事件
包括KEYUP、KEYDOWN
响应按键按下：查看KEYDOWN事件
响应按键事件的方式是**标志变量**
当按下空格键时 设置space_key=true的标志，
释放时space_key=false
不必再事件发生时立即响应，可以响应标志变量
退出键  Escape

pygame不会重复响应被按下的键，仅仅在第一次按下时发送事件
一个键按下时重复响应：pygame.key.set_repeat(10),参数是ms为单位的重复值

4。2.3鼠标事件
MOUSEMOTION 事件：属性是event.pos  event.rel  event.buttons

MOUSEBUTTONUP 事件：
MOUSEBUTTONDOWN


4.3设备轮询
检测用户输入，pygame的事件系统，轮询输入设备，用户与程序交互
pygame.key.get_pressed()返回布尔值的列表，每个键一个标志
使用键常量值索引布尔值数组

