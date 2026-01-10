from opensearchpy import OpenSearch  
client = OpenSearch('http://localhost:9200')  
mapping = {  
  "mappings": {  
    "properties": {  
      "@timestamp": {"type": "date", "format": "strict_date_optional_time||epoch_millis"},  
      "tenant": {"type": "keyword"},  
      "source": {"type": "keyword"},  
      "vendor": {"type": "keyword"},  
      "product": {"type": "keyword"},  
      "event_type": {"type": "keyword"},  
      "event_subtype": {"type": "keyword"},  
      "severity": {"type": "integer"},  
      "action": {"type": "keyword"},  
      "src_ip": {"type": "ip"},  
      "src_port": {"type": "integer"},  
      "dst_ip": {"type": "ip"},  
      "dst_port": {"type": "integer"},  
      "protocol": {"type": "keyword"},  
      "user": {"type": "keyword"},  
      "host": {"type": "keyword"},  
      "process": {"type": "keyword"},  
      "url": {"type": "keyword"},  
      "http_method": {"type": "keyword"},  
      "status_code": {"type": "integer"},  
      "rule_name": {"type": "keyword"},  
      "rule_id": {"type": "keyword"},  
      "cloud.account_id": {"type": "keyword"},  
      "cloud.region": {"type": "keyword"},  
      "cloud.service": {"type": "keyword"},  
      "raw": {"type": "text"},  
      "_tags": {"type": "keyword"},  
      "geo": {"type": "object"}  
    }  
  }  
}  
client.indices.create(index='logs-*', body=mapping)  