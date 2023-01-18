import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

const imageApi = createApi({
  reducerPath: 'imageApi',
  baseQuery: fetchBaseQuery({
    baseUrl: '/api',
  }),
  endpoints: (build) => ({
    
  }),
});

export const { } = imageApi;

export default imageApi;
