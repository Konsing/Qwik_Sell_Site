import { ApplicationConfig } from '@angular/core';
import { provideHttpClient } from '@angular/common/http';

export const config: ApplicationConfig = {
  providers: [
    provideHttpClient(),
    // Add other providers here if needed
  ],
};
