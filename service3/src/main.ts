import { NestFactory } from '@nestjs/core';
import { Transport,MicroserviceOptions } from '@nestjs/microservices';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.createMicroservice<MicroserviceOptions>(AppModule, {
  transport: Transport.RMQ,
  options: {
    urls: ['amqps://hegzpijz:wP6xyaCkVI8M-ETfBYcYEY5Se9eqvTAE@rat.rmq2.cloudamqp.com/hegzpijz'],
    queue: 'queue2',
    queueOptions: {
      durable: false
    },
  },
});
  await app.listen();
}
bootstrap();
