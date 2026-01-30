
import fetch from 'node-fetch';
import fs from 'fs';

const config = JSON.parse(fs.readFileSync('/Users/yixuanzhang/.dida-mcp-config.json', 'utf8'));
const token = config.access_token;
const inboxId = config.inboxId;

async function run() {
    console.log("=== Testing V1 Update Capability ===");
    if (!token) {
        console.error("No V1 Token found!");
        return;
    }

    // 1. Find a task to update (in Inbox)
    console.log(`Listing tasks in Inbox (${inboxId})...`);
    const listRes = await fetch(`https://api.dida365.com/open/v1/project/${inboxId}/task`, {
        headers: { Authorization: `Bearer ${token}` }
    });

    if (!listRes.ok) {
        console.error("List failed:", listRes.status, await listRes.text());
        return;
    }

    const tasks: any = await listRes.json();
    const target = (Array.isArray(tasks) ? tasks : []).find((t: any) => !t.completedTime); // Find active task

    if (!target) {
        console.error("No active tasks found in inbox to test with.");
        return;
    }

    console.log(`Target Task: [${target.title}] (${target.id})`);
    const originalTitle = target.title;
    const newTitle = originalTitle + " [V1 UPDATED]";

    // 2. Try Update Strategy A: Simple Partial Object
    console.log("\n--- Attempting Update Strategy A (POST /task/{id} with partial body) ---");
    const updateRes = await fetch(`https://api.dida365.com/open/v1/task/${target.id}`, {
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title: newTitle })
    });

    console.log(`Update A Status: ${updateRes.status}`);
    console.log(`Update A Response:`, await updateRes.text());

    // 3. Verify
    const verifyRes = await fetch(`https://api.dida365.com/open/v1/project/${inboxId}/task/${target.id}`, {
        headers: { Authorization: `Bearer ${token}` }
    });
    const verifiedTask: any = await verifyRes.json();

    if (verifiedTask.title === newTitle) {
        console.log("✅ SUCCESS! V1 Update worked with Strategy A.");
        return;
    } else {
        console.log(`❌ Failed. Title is still: "${verifiedTask.title}"`);
    }

    // 4. Try Strategy B: Full Object
    console.log("\n--- Attempting Update Strategy B (Full Object) ---");
    const fullUpdateBody = {
        ...target,
        title: newTitle + " B",
        projectId: inboxId
    };
    // remove read-only fields
    delete (fullUpdateBody as any).permission;
    delete (fullUpdateBody as any).etag;

    const updateBRes = await fetch(`https://api.dida365.com/open/v1/task/${target.id}`, {
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(fullUpdateBody)
    });
    console.log(`Update B Status: ${updateBRes.status}`);
    console.log(`Update B Response:`, await updateBRes.text());

    // Verify B
    const verifyBRes = await fetch(`https://api.dida365.com/open/v1/project/${inboxId}/task/${target.id}`, {
        headers: { Authorization: `Bearer ${token}` }
    });
    const verifiedTaskB: any = await verifyBRes.json();
    if (verifiedTaskB.title.includes("B")) {
        console.log("✅ SUCCESS! V1 Update worked with Strategy B.");
        return;
    } else {
        console.log(`❌ Failed. Title is still: "${verifiedTaskB.title}"`);
    }
}

run();
