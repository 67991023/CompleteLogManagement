from fastapi import FastAPI, Depends, HTTPException, Request  
from fastapi.security import HTTPBearer  
from opensearchpy import OpenSearch  
import jwt  
from datetime import datetime, timedelta  
from alert import scheduler