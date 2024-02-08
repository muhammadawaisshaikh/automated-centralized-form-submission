import Home from '../components/Home.vue';
import FormSubmissions from '../components/FormSubmissions.vue';
import DataCollectionForm from '../components/DataCollectionForm.vue';

const routes = [
  { path: '/', component: Home },
  { path: '/form-submissions', component: FormSubmissions },
  { path: '/data-collection-form', component: DataCollectionForm }
];

export default routes;