import { Controller, Get } from '@nestjs/common';
import { AppService } from './app.service';

import { MessagePattern, Payload, Ctx, RmqContext } from '@nestjs/microservices';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}


  @MessagePattern('service3')
  getNotifications(@Payload() data: string, @Ctx() context: RmqContext) {
  console.log(data);
  }
}
