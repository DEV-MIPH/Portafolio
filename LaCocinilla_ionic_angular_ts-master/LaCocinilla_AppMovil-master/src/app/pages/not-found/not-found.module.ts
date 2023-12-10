import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { NotFoundPageRoutingModule } from './not-found-routing.module';

import { NotFoundPage } from './not-found.page';

import { defineCustomElements } from '@teamhive/lottie-player/loader';
import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    NotFoundPageRoutingModule
  ],
  declarations: [NotFoundPage],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
})
export class NotFoundPageModule {}
