import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { LoginPageRoutingModule } from './login-routing.module';

import { LoginPage } from './login.page';

import { defineCustomElements } from '@teamhive/lottie-player/loader';
import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';

defineCustomElements(window);
@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    LoginPageRoutingModule
  ],
  declarations: [LoginPage], 
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
})
export class LoginPageModule {}