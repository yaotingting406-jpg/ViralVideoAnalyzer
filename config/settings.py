"""项目全局配置文件"""
import os
from dotenv import load_dotenv

load_dotenv()

# API配置
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')

# 数据目录
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
RAW_DATA_DIR = os.path.join(DATA_DIR, 'raw')
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed')
OUTPUT_DIR = os.path.join(DATA_DIR, 'outputs')

# 创建目录
for dir_path in [RAW_DATA_DIR, PROCESSED_DATA_DIR, OUTPUT_DIR]:
    os.makedirs(dir_path, exist_ok=True)

# 视频下载配置
VIDEO_QUALITY = 'best'
MAX_VIDEO_DURATION = 600
MIN_VIDEO_DURATION = 5

# 特征提取配置
SAMPLE_RATE = 24
COLOR_CLUSTERS = 5

# AI生成配置
AI_MODEL = 'gpt-4'
MAX_SCRIPT_LENGTH = 1000
TEMPERATURE = 0.7

# 日志配置
LOG_LEVEL = 'INFO'
LOG_FILE = 'logs/viral_analyzer.log'
