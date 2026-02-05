import json

def clean_web_data(raw_input):
    """
    数据清洗与结构化模块
    用于解析多层嵌套JSON并提取网页基础信息
    """

    debug_log = []
    final_list = []

    try:
        # 第一层解析
        if isinstance(raw_input, str):
            level_1_data = json.loads(raw_input)
        else:
            level_1_data = raw_input
        debug_log.append("Level 1 unpacked")

        # 第二层解析
        if isinstance(level_1_data, dict) and "raw_output" in level_1_data:
            inner_json_str = level_1_data["raw_output"]
            if isinstance(inner_json_str, str):
                level_2_data = json.loads(inner_json_str)
            else:
                level_2_data = inner_json_str
            debug_log.append("Level 2 unpacked (raw_output)")
        else:
            level_2_data = level_1_data

        # 第三层提取目标字段
        if isinstance(level_2_data, dict):
            if "Basic information of web pages" in level_2_data:
                final_list = level_2_data["Basic information of web pages"]
                debug_log.append("Target field found")
            else:
                first_key = list(level_2_data.keys())[0]
                final_list = level_2_data[first_key]
                debug_log.append("Fallback key used")

        elif isinstance(level_2_data, list):
            final_list = level_2_data
            debug_log.append("Direct list found")

    except Exception as e:
        debug_log.append(f"Error: {str(e)}")

    return {
        "clean_data": final_list,
        "count": len(final_list),
        "debug_trace": " | ".join(debug_log),
        "status": "success" if len(final_list) > 0 else "empty"
    }
