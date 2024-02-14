import Home from '../components/Home.vue';
import FormSubmissions from '../components/FormSubmissions.vue';
import DataCollectionForm from '../components/DataCollectionForm.vue';
import TestForm01 from '../components/TestForm01.vue';

const routes = [
  { path: '/', component: Home },
  { path: '/form-submissions', component: FormSubmissions },
  { path: '/data-collection-form', component: DataCollectionForm },
  { path: '/test-form-01', component: TestForm01 }
];

export default routes;