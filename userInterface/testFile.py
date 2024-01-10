from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsPixmapItem, QApplication
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

app = QApplication([])

# 创建 QGraphicsScene 和 QGraphicsView
scene = QGraphicsScene()
view = QGraphicsView(scene)

# 创建 QPixmap 对象并加载图片
img = QPixmap('hello.jpg')

# 创建 QGraphicsPixmapItem，并将图片添加到场景
pixmap_item = QGraphicsPixmapItem(img)
scene.addItem(pixmap_item)

# 设置视图属性
view.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
view.setSceneRect(pixmap_item.pixmap().rect())

# 显示视图
view.show()

# 运行应用程序
app.exec()
