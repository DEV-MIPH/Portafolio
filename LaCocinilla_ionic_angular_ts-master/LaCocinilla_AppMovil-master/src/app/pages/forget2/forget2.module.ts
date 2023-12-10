import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { Forget2PageRoutingModule } from './forget2-routing.module';

import { Forget2Page } from './forget2.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    Forget2PageRoutingModule
  ],
  declarations: [Forget2Page]
})
export class Forget2PageModule {}
