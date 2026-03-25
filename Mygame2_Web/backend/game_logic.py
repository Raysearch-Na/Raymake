from config import config


fake_database = {
    "player_1": {
        "funds": config.INITIAL_FUNDS,
        "stamina": config.INITIAL_STAMINA
    }
}


def do_work_action(user_id: str):
    """打工"""
    player = fake_database.get(user_id)
    if not player:
        return {"error": "玩家不存在"}

    # 获取 config.py 中的配置
    cost = config.ACTION_WORK["stamina_cost"]
    reward = config.ACTION_WORK["base_reward"]

    # 核心逻辑判断
    if player["stamina"] < cost:
        return {"error": "体力不足，无法打工！"}

    # 执行数值扣除与增加
    player["stamina"] -= cost
    # 这里我们演示一下全局倍率的用法
    actual_reward = int(reward * config.GLOBAL_INCOME_MULTIPLIER)
    player["funds"] += actual_reward

    return {
        "message": "打工成功！",
        "current_funds": player["funds"],
        "current_stamina": player["stamina"],
        "earned": actual_reward
    }
