import { Inject,Injectable } from '@nestjs/common';
import { ClientProxy } from '@nestjs/microservices'

@Injectable()
export class AppService {
  constructor(
    @Inject('CLIENT_SERVICE') private client: ClientProxy
  ){}


}
