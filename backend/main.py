import logging
import os
import sys

import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define, options
from tornado.web import StaticFileHandler

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)
from backend.tools.get_host_ip import host_ip
from backend.tools import log

logger = logging.getLogger(log.LOGGER_ROOT_NAME + '.' + __name__)

current_path = os.path.dirname(__file__)
settings = dict(
    # debug=True,
    static_path=os.path.join(current_path, "dist")  # 配置静态文件路径
)


def make_app():
    from backend.webInterface import yolov5web_run
    from backend.webInterface import yolov5web_index

    return tornado.web.Application([
        (r"/api/yolov5-run/", yolov5web_run.Yolov5webRun),
        (r"/", yolov5web_index.Index),
        (r"/(.*)", StaticFileHandler,
         {"path": os.path.join(current_path, "dist"), "default_filename": "index.html"}),

    ], **settings)


if __name__ == "__main__":
    define("port", default=8091, type=int, help='指定运行时端口号')

    tornado.options.parse_command_line()
    port = options.port
    app = make_app()

    server = tornado.httpserver.HTTPServer(app)
    # server.listen(port)
    server.bind(port)
    server.start(1)
    print(f'Server is running: http://{host_ip()}:{port}')

    # tornado.ioloop.IOLoop.instance().start()
    tornado.ioloop.IOLoop.current().start()
