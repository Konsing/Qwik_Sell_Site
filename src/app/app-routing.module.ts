import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { ProductListComponent } from './product-list/product-list.component';
import { AddProductComponent } from './add-product/add-product.component';

export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'product-list', component: ProductListComponent },
  { path: 'add-product', component: AddProductComponent },
  { path: '**', redirectTo: '', pathMatch: 'full' } // wildcard route for a 404 page
];
