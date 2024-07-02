import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';
import { provideRouter } from '@angular/router';
import { routes } from './app/app-routing.module';
import { config } from './app/app.config.server';  // Import the correct configuration

bootstrapApplication(AppComponent, {
  providers: [
    provideRouter(routes),
    ...config.providers,  // Spread the providers from the config
  ]
}).catch(err => console.error(err));
