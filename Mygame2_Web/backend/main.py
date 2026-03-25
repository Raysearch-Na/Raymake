# backend/main.py
from fastapi import FastAPI
from game_logic import do_work_action, fake_database
from fastapi.middleware.cors import CORSMiddleware

# 创建一个 FastAPI 实例
app = FastAPI(title=" Raymake ")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有网页访问（开发环境最方便）
    allow_methods=["*"],
    allow_headers=["*"],
)

# 获取玩家当前状态的接口
@app.get("/api/player/status")
async def get_player_status():
    # 暂时默认返回 player_1 的数据
    return fake_database["player_1"]

# 执行打工动作的接口 (使用 POST 方法表示改变了服务器状态)
@app.post("/api/action/work")
async def work():
    # 调用我们刚刚写的业务逻辑
    result = do_work_action(user_id="player_1")
    return result