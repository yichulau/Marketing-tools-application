import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as lambda from 'aws-cdk-lib/aws-lambda';
// import * as sqs from 'aws-cdk-lib/aws-sqs';

export class InfraStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // The code that defines your stack goes here
    const layer = new lambda.LayerVersion(this, "BasLayer", {
      code: lambda.Code.fromAsset("lambda_base_layer/layer.zip"),
      compatibleRuntimes:[lambda.Runtime.PYTHON_3_9],
    });
    // example resource
    const apiLambda= new lambda.Function(this, 'ApiFunction', {
      code: lambda.Code.fromAsset("../app/"),
      handler: 'main_api.handler',
      runtime: lambda.Runtime.PYTHON_3_9,
      layers: [layer]
    });
  }
}
