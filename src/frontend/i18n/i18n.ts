import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import LanguageDetector from 'i18next-browser-languagedetector';

// Import translation files
import enCommon from './locales/en/common.json';

const resources = {
  en: {
    common: enCommon,
  },
  // Add more languages as needed
  // es: {
  //   common: esCommon,
  // },
  // fr: {
  //   common: frCommon,
  // },
};

i18n
  .use(LanguageDetector)
  .use(initReactI18next)
  .init({
    resources,
    fallbackLng: 'en',
    debug: process.env.NODE_ENV === 'development',
    
    interpolation: {
      escapeValue: false, // React already escapes values
    },
    
    detection: {
      // Order and from where user language should be detected
      order: ['localStorage', 'navigator', 'htmlTag'],
      
      // Keys or params to lookup language from
      lookupLocalStorage: 'i18nextLng',
      lookupFromPathIndex: 0,
      lookupFromSubdomainIndex: 0,
      
      // Cache user language on
      caches: ['localStorage'],
      excludeCacheFor: ['cimode'], // Languages to not persist (cookie, localStorage)
      
      // Optional expire and domain for set cookie
      cookieMinutes: 10,
      cookieDomain: 'myDomain',
      
      // Optional htmlTag with lang attribute, the default is:
      htmlTag: document.documentElement,
      
      // Optional set cookie options, reference:[MDN Set-Cookie docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie)
      cookieOptions: { path: '/', sameSite: 'strict' }
    },
    
    react: {
      useSuspense: false,
    },
  });

export default i18n; 