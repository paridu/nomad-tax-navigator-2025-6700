resource "aws_db_instance" "tax_db" {
  allocated_storage    = 20
  identifier           = "compliance-compass-db"
  db_name              = "tax_engine_db"
  engine               = "postgres"
  engine_version       = "15.3"
  instance_class       = "db.t3.micro"
  username             = var.db_username
  password             = var.db_password
  parameter_group_name = "default.postgres15"
  skip_final_snapshot  = true
  storage_encrypted    = true

  tags = {
    Name = "GlobalComplianceCompass-DB"
  }
}

resource "aws_elasticache_cluster" "tax_cache" {
  cluster_id           = "tax-engine-cache"
  engine               = "redis"
  node_type            = "cache.t3.micro"
  num_cache_nodes      = 1
  parameter_group_name = "default.redis7"
  port                 = 6379
}