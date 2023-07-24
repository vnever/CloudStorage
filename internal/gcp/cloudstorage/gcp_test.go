package cloudstorage

import (
    "context"
    "testing"
    cloudtasks "google.golang.org/api/cloudtasks/v2"
)

func FetchCloudTaskQueue(ctx context.Context, projectID, locationID, queueID string) (*cloudtasks.Queue, error) {
    service, err := cloudtasks.NewService(ctx)
    if err != nil {
        return nil, err
    }

    name := "projects/" + projectID + "/locations/" + locationID + "/queues/" + queueID
    queue, err := service.Projects.Locations.Queues.Get(name).Context(ctx).Do()
    if err != nil {
        return nil, err
    }

    return queue, nil
}

func TestCreateCloudTaskQueue(t *testing.T) {
    ctx := context.Background() // Create a context

    queue := &cloudtasks.Queue{
        Name:  "my-queue",
        RateLimits: &cloudtasks.RateLimits{
            MaxBurstSize:           100,
            MaxConcurrentDispatches: 50,
            MaxDispatchesPerSecond:  10.0,
        },
        RetryConfig: &cloudtasks.RetryConfig{
            MaxAttempts: 5,
            MaxBackoff:  "10s",
            MinBackoff:  "1s",
        },
    }

    // Create the Cloud Task queue
    createdQueue, err := CreateCloudTaskQueue(ctx, "my-project", "us-central1", queue)
    if err != nil {
        t.Fatalf("Failed to create Cloud Task queue: %v", err)
    }
    if createdQueue == nil {
        t.Fatal("Created queue is nil")
    }
}

func TestUpdateCloudTaskQueue(t *testing.T) {
    ctx := context.Background() // Create a context

    // Fetch queue
    existingQueue, err := FetchCloudTaskQueue(ctx, "my-project", "us-central1", "my-queue")
    if err != nil {
        t.Fatalf("Failed to fetch existing Cloud Task queue: %v", err)
    }

    // Modify property in queue
    existingQueue.RateLimits.MaxBurstSize = 200

    // Update queue
    updatedQueue, err := UpdateCloudTaskQueue(ctx, "my-project", "us-central1", "my-queue", existingQueue)
    if err != nil {
        t.Fatalf("Failed to update Cloud Task queue: %v", err)
    }
    if updatedQueue == nil {
        t.Fatal("Updated queue is nil")
    }
}
