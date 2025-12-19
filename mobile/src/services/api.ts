import axios from 'axios';

const API_URL = 'http://localhost:8000/api/v1';

const apiClient = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const reportEmergency = async (data: any) => {
  const response = await apiClient.post('/emergency/', data);
  return response.data;
};

export const getMyCases = async () => {
  const response = await apiClient.get('/emergency/');
  return response.data.cases || [];
};

export const getCaseById = async (caseId: string) => {
  const response = await apiClient.get(`/emergency/${caseId}`);
  return response.data;
};

export default apiClient;

