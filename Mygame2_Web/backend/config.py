class GameConfig:
    TICK_RATE = 1.0  # 游戏内部循环的步长（秒），比如每1秒结算一次收益

    # 玩家初始属性
    INITIAL_FUNDS = 100  # 初始资金
    INITIAL_STAMINA = 200  # 初始体力

    # 经济系统全局倍率
    GLOBAL_INCOME_MULTIPLIER = 1.0  # 全局收益倍率
    GLOBAL_COST_MULTIPLIER = 1.0  # 全局消耗倍率

    # 打工
    ACTION_WORK = {
        "stamina_cost": 10,  # 每次打工消耗体力
        "base_reward": 50,  # 基础获得资金
        "cooldown": 5  # 冷却时间（秒）
    }


# 实例化
config = GameConfig()