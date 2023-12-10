import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { Forget2Page } from './forget2.page';

const routes: Routes = [
  {
    path: '',
    component: Forget2Page
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class Forget2PageRoutingModule {}
