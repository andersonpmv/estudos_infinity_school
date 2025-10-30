// supabaseClient.js
import { createClient } from "https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/+esm";

// 🔐 Dados do seu projeto Supabase
const SUPABASE_URL = 'https://zvwfklxunqjktjddwary.supabase.co';
const SUPABASE_ANON_KEY =
  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inp2d2ZrbHh1bnFqa3RqZGR3YXJ5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjA5ODQ4MDcsImV4cCI6MjA3NjU2MDgwN30.7D8ewHkItKber_g7bXjRE6-Rs5tanYR2Z-7l3YLU9Fo';

export const supabase = createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
window.supabase = supabase; // garante acesso global

console.log("✅ Supabase Client inicializado:", supabase);