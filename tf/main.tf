resource "aws_sns_topic" "stock_updates" {
  name = "stock-update-topic"
}

resource "aws_sns_topic_subscription" "user_updates_sqs_target" {
  topic_arn = aws_sns_topic.stock_updates.arn
  protocol  = "sms"
  endpoint  = var.user_contact
}

