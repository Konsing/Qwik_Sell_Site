import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';
import { provideRouter } from '@angular/router';
import { routes } from './app/app-routing.module';
import { config } from './app/app.config.server';
import { ApplicationRef } from '@angular/core';

export function bootstrap(): Promise<ApplicationRef> {
  return bootstrapApplication(AppComponent, {
    providers: [
      provideRouter(routes),
      ...config.providers,
    ]
  });
}

// Add a default export for Vite compatibility
export default bootstrap;
